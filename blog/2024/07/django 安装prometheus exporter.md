---
slug: django 安装prometheus exporter
title: django 安装prometheus exporter
date: 2024-07-25T01:00:00
authors:
  - timger
tags:
  - k8s
  - django
---
https://github.com/korfuri/django-prometheus

新增路径

```python
path('prometheus/', include('django_prometheus.urls')),
```

查看

http://0.0.0.0:8101/prometheus/metrics

最后想了想

其实在 nginx  上装就行了 
放弃

