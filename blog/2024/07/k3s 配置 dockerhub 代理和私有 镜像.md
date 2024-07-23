---
slug: k3s-docker-register-mirror-proxy
title: k3s 拉取私有镜像 和 代理镜像配置
authors:
  - timger
tags:
  - docker
  - k3s
  - k8s
---

写在 2024 年 7 月 docker hub 被墙之后

`/etc/rancher/k3s/registries.yaml`

```yaml
mirrors:
  registry.dafengstudio.cn:
    endpoint:
      - "https://registry.dafengstudio.cn"
  docker.io:
	endpoint:
      - https://docker.m.daocloud.io
      - https://huecker.io
      - https://dockerhub.timeweb.cloud
      - https://noohub.ru
configs:
  "registry.dafengstudio.cn":
    auth:
      username: xxx
      password: xxxx
```


然后记得重启

1. `service k3s restart`
2. `service k3s-agent restart`