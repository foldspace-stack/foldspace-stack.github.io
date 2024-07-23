---
slug: promtail-k8s-log
title: promtail 收集 k8s 日志踩坑
authors:
  - timger
tags:
  - docker
  - k8s
---
创建服务账号

```yml
apiVersion: v1

kind: ServiceAccount

metadata:

name: promtail-serviceaccount

namespace: monitor

  

---

apiVersion: rbac.authorization.k8s.io/v1

kind: ClusterRole

metadata:

name: promtail-clusterrole

#namespace: monitor

rules:

- apiGroups: [""]

resources:

- nodes

- services

- pods

- namespaces

- configmaps

- jobs

- cronjobs

- persistentvolumeclaims

- ingresses

- deployments

- replicationcontrollers

verbs:

- get

- watch

- list

- apiGroups:

- apps

resources:

- deployments

verbs:

- get

- list

- watch

  

---

apiVersion: rbac.authorization.k8s.io/v1

kind: ClusterRoleBinding

metadata:

name: promtail-clusterrolebinding

#namespace: monitor

subjects:

- kind: ServiceAccount

name: promtail-serviceaccount

namespace: monitor

- kind: User

name: danny

#- kind: ServiceAccount

# name: promtail-serviceaccount

# namespace: foldspace-apps

#- kind: ServiceAccount

# name: promtail-serviceaccount

# namespace: default

#- kind: ServiceAccount

# name: promtail-serviceaccount

# namespace: dapr-system

#- kind: ServiceAccount

# name: promtail-serviceaccount

# namespace: openfunction

#- kind: ServiceAccount

# name: promtail-serviceaccount

# namespace: kube-system

#- kind: ServiceAccount

# name: promtail-serviceaccount

# namespace: kubernetes-dashboard

#- kind: ServiceAccount

# name: promtail-serviceaccount

# namespace: kube-public

#- kind: ServiceAccount

# name: promtail-serviceaccount

# namespace: ingress-apisix

roleRef:

kind: ClusterRole

name: promtail-clusterrole

#name: admin

apiGroup: rbac.authorization.k8s.io
```

创建部署

```yaml
apiVersion: v1

kind: ConfigMap

metadata:

name: promtail-configmap

namespace: monitor

data:

promtail.yaml: |-

server:

http_listen_port: 9080

grpc_listen_port: 0

  

positions:

filename: /tmp/positions.yaml

  

clients:

- url: http://192.168.31.203:3100/loki/api/v1/push #${ip}填入loki的对应地址

  

scrape_configs:

- job_name: kubernetes-pods-app

pipeline_stages:

- docker: {}

kubernetes_sd_configs:

- role: pod

relabel_configs:

- action: drop

regex: .+

source_labels:

- __meta_kubernetes_pod_label_name

- source_labels:

- __meta_kubernetes_pod_label_app

target_label: __service__

- source_labels:

- __meta_kubernetes_pod_node_name

target_label: __host__

- action: replace

replacement: $1

separator: /

source_labels:

- __meta_kubernetes_namespace

- __meta_kubernetes_pod_name

target_label: job

- action: replace

source_labels:

- __meta_kubernetes_namespace

target_label: namespace

- action: drop

regex: ''

source_labels:

- __service__

- action: labelmap

regex: __meta_kubernetes_pod_label_(.+)

- replacement: /var/log/pods/*$1/*.log

separator: /

source_labels:

- __meta_kubernetes_pod_uid

- __meta_kubernetes_pod_container_name

target_label: __path__

  
  

---

apiVersion: apps/v1

kind: DaemonSet

metadata:

name: promtail-log-collector

namespace: monitor

labels:

app: promtail

spec:

selector:

matchLabels:

app: promtail

type: daemonset

author: danny

template:

metadata:

labels:

app: promtail

type: daemonset

author: danny

spec:

containers:

- name: promtail

image: registry.dafengstudio.cn/grafana/promtail:2.9.2

args:

- -config.file=/etc/promtail/promtail.yaml

- -config.expand-env=true

env:

- name: HOSTNAME

valueFrom:

fieldRef:

apiVersion: v1

fieldPath: spec.nodeName

- name: TZ

value: Asia/Shanghai

ports:

- containerPort: 3101

name: http-metrics

protocol: TCP

securityContext:

#readOnlyRootFilesystem: true

runAsGroup: 0

runAsUser: 0

volumeMounts:

- mountPath: /etc/promtail

name: promtail-configmap

- mountPath: /run/promtail

name: run

- mountPath: /var/lib/kubelet/pods

name: kubelet

readOnly: true

- mountPath: /var/lib/docker/containers

name: docker

readOnly: true

- mountPath: /var/log/pods

name: pod-log

readOnly: true

- name: timezone

mountPath: /etc/localtime

volumes:

- configMap:

defaultMode: 420

name: promtail-configmap

name: promtail-configmap

- name: timezone

hostPath:

path: /usr/share/zoneinfo/Asia/Shanghai

- hostPath:

path: /run/promtail

type: ""

name: run

- hostPath:

path: /var/lib/kubelet/pods

type: ""

name: kubelet

- hostPath:

path: /var/lib/docker/containers

type: ""

name: docker

- hostPath:

path: /var/log/pods

type: ""

name: pod-log

serviceAccount: promtail-serviceaccount

serviceAccountName: promtail-serviceaccount

updateStrategy:

type: RollingUpdate
```

最后发现 好几个 namespace 的 日志怎么也收集不上开

![](attachments/Pasted%20image%2020240723132229.png)

原来发现必须要 打标 app 才可以收到

![](attachments/Pasted%20image%2020240723132309.png)

https://github.com/grafana/loki/issues/353