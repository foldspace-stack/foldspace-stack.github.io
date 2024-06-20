---
slug: docker 被封之后 如何访问
title: docker 被封之后 如何访问
authors: timger
tags:
  - docker
---
修改 daemon 配置
加入如下内容.

```bash
mkdir -p /etc/docker
vim /etc/docker/daemon.json <<-'EOF'
{
    "registry-mirrors": [
        "https://docker.m.daocloud.io",
        "https://huecker.io",
        "https://dockerhub.timeweb.cloud",
        "https://noohub.ru"
    ]
}
```