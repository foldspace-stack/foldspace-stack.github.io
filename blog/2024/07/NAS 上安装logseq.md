---
slug: NAS 上安装logseq
title: NAS 上安装logseq
date: 2024-07-30T19:02:00
authors:
  - timger
tags:
  - docker
  - bitwarden
  - nas
---
# 简介

[Logseq](https://logseq.com/)是一个**知识管理**和**协作**平台。它专注于隐私**、**持久**性**和[**用户控制**](https://www.gnu.org/philosophy/free-sw.en.html)。Logseq 提供了一系列强大的**知识管理**、**协作**、**PDF 注释**和**任务管理****工具**，支持多种文件格式，包括**Markdown**和**Org-mode**，以及用于组织和构建笔记的**各种功能。**

Logseq 的**白板**功能可让您使用带有**形状**、**绘图**、**网站嵌入**和**连接器的空间****画布**来组织您的知识和想法。您可以**直观地分组**和**链接**您的**笔记**和外部媒体（例如**视频**和**图像**），使视觉思考者能够以新的方式撰写、重新混合、**注释**和连接来自其知识库和新兴想法的内容。

除了核心功能外，Logseq 还拥有不断壮大的**插件**和**主题**生态系统，可实现各种工作流程和**自定义**选项。还提供**移动应用程序**，可访问桌面应用程序的大多数功能。无论您是学生、专业人士，还是任何重视以清晰、有条理的方式管理想法和笔记的人，Logseq 都是任何希望提高工作效率和简化工作流程的人的绝佳选择。

https://github.com/logseq/logseq

# 安装

在 nas 上执行

```bash
Status: Downloaded newer image for registry.dafengstudio.cn/logseq/logseq-webapp:latest
registry.dafengstudio.cn/logseq/logseq-webapp:latest
ash-4.3# docker pull registry.dafengstudio.cn/bitwarden/server:latest
latest: Pulling from bitwarden/server
efc2b5ad9eec: Downloading [===========================>                       ]  16.22MB/29.13MB
66b672aaa3a6: Downloading [=======================>                           ]   8.65MB/18.71MB
3d7d086377ca: Download complete
030dfb09a3db: Downloading [===============================>                   ]  20.32MB/32.24MB
75cceec2ae3f: Waiting
2fe3f9fcc07a: Waiting
5005e22762b0: Waiting
```

注意 最近 docker 被强
自己找加速器 下载后 再推到私有

```bash
docker pull hub.uuuadc.top/bitwarden/server 
docker image tag hub.uuuadc.top/bitwarden/server:latest registry.dafengstudio.cn/bitwarden/server:
docker push registry.dafengstudio.cn/bitwarden/server:latest
```

挂载目录

```
WORKDIR /data
```

# nas 安装

```shell
docker run --name tream-logseq  \
	-it -d \
	--restart=always \
    -p 3001:80 \
    -v /volume1/docker/foldspace-apps/tream-logseq/:/data \
    registry.dafengstudio.cn/logseq/logseq-webapp:latest
```


http://192.168.31.88:3001/#/

![](attachments/Pasted%20image%2020240730160105.png)


### 错误It seems that your browser doesn't support the [new native filesystem API](https://web.dev/file-system-access/), please use any Chromium 86+ based browser like Chrome, Vivaldi, Edge, etc. Notice that the API doesn't support mobile browsers at the moment.
![](attachments/Pasted%20image%2020240730160238.png)


# 参考
1. https://github.com/logseq/logseq/blob/master/docs/docker-web-app-guide.md
2. https://github.com/logseq/logseq/blob/master/Dockerfile