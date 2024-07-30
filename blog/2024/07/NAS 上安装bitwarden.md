---
slug: NAS 上安装bitwarden
title: NAS 上安装bitwarden
date: 2024-07-30T19:02:00
authors:
  - timger
tags:
  - docker
  - bitwarden
  - nas
---
# 简介

Bitwarden 是一款开源的密码管理工具，提供跨平台的密码管理解决方案。用户可以安全地存储敏感信息，如密码、信用卡信息和笔记，并通过加密保护这些信息。Bitwarden 支持自动填充密码、生成强密码、共享安全信息等功能，同时提供浏览器插件、移动应用和桌面应用，方便用户在不同设备上访问和管理密码。Bitwarden 的安全性建立在端到端加密和零知识架构之上，确保用户的数据得到最高级别的保护。

# 安装

注意 最近 docker 被强
自己找加速器 下载后 再推到私有

```bash
docker pull hub.uuuadc.top/bitwarden/server 
docker image tag hub.uuuadc.top/bitwarden/server:latest registry.dafengstudio.cn/bitwarden/server:
docker push registry.dafengstudio.cn/bitwarden/server:latest
```

挂载目录

```
WORKDIR /opt/bitwarden
```


![](attachments/Pasted%20image%2020240730155318.png)
# nas 安装

admin token 生成

https://github.com/dani-garcia/vaultwarden/wiki/Enabling-admin-page#secure-the-admin_token

```
docker exec -it bitwarden-server /vaultwarden hash
```

run

```bash
docker stop bitwarden-server|true
docker rm bitwarden-server
```

```shell

docker run \
	--name bitwarden-server \
	 -d \
	--restart=always \
	-e WEBSOCKET_ENABLED=true \
	-e SIGNUPS_ALLOWED=false \
	-e I_REALLY_WANT_VOLATILE_STORAGE=true \
	-e  ADMIN_TOKEN='$argon2id$v=19$m=65540,t=3,p=4$UhMyL86++kz+P9BmkHYFB8DmflBNrWnkcrAYRYTCR4c$YGSGH494PLQkXyiRJ9wFfeXbQREPwsZsmJArEQqKtlg' \
	  -p 3013:80 \
	  -p 3012:3012 \
    -v /volume1/docker/foldspace-apps/bitwarden:/data/ \
    registry.dafengstudio.cn/vaultwarden/server:latest
```

# 参考
1. https://zx1.fun/2022/09/21/%E4%BD%BF%E7%94%A8docker%E6%90%AD%E5%BB%BA%E8%87%AA%E5%B7%B1%E7%9A%84bitwarden%E5%AF%86%E7%A0%81%E7%AE%A1%E7%90%86%E6%9C%8D%E5%8A%A1/
2. https://hub.docker.com/r/vaultwarden/server
3. https://frameworks.readthedocs.io/en/latest/devops/vaultwardenDocker.html
4. https://github.com/dani-garcia/vaultwarden