---
slug: 在容器中运行 winxp 使用docker 运行 winxp 和 win7
title: 在容器中运行 winxp 使用docker 运行 winxp 和 win7
date: 2024-08-19T13:00:00
authors:
  - timger
tags:
  - docker
  - winxp
  - win7
---
# 简介

dockur/windows 是一个容器化的 win 项目

https://github.com/dockur/windows

特点✨
多语言
ISO 下载器
KVM加速
基于 Web 的查看器

# 安装

## 镜像

```bash
docker pull ghcr.io/dockur/windows:3.13

```

运行
```bash
docker run \
	-it --rm \
	-p 8006:8006  \
	--cap-add NET_ADMIN \
	-e VERSION='winxp' \
	-e KVM="N" \
	-e RAM_SIZE='1G' \
	--stop-timeout 120 \
	ghcr.io/dockur/windows:3.13
```

http://127.0.0.1:8006/?resize=scale&autoconnect=true

他这个 本身使用的事 vnc 技术

![](attachments/Pasted%20image%2020240819164425.png)

![](attachments/Pasted%20image%2020240819170345.png)

![](attachments/Pasted%20image%2020240819193841.png)

## win7


## 改为 可以 开箱即用的镜像

```
docker commit b46f8da3f4f4 registry.dafengstudio.cn/windows:xp
docker push  registry.dafengstudio.cn/windows:xp
```