# 简介

`docker-mailserver` 是一个开源项目，旨在简化邮件服务器的部署和管理。它是一个基于 Docker 的邮件服务器解决方案，允许用户快速搭建和运行功能齐全的邮件服务器，支持多种邮件协议（如 IMAP 和 SMTP），并提供多种功能和配置选项。

### 主要特性

1. **易于部署**：通过 Docker，用户可以快速部署邮件服务器，而不需要复杂的安装和配置过程。

2. **多种邮件协议支持**：支持 IMAP、SMTP 和 POP3 协议，允许用户访问和管理邮件。

3. **内置安全功能**：支持 SSL/TLS 加密、反垃圾邮件和反病毒功能，确保邮件通信的安全性。

4. **用户管理**：支持通过环境变量或 API 管理用户和域名，便于用户的添加、删除和管理。

5. **集成工具**：可以与其他工具集成，例如 Dovecot（IMAP/POP3 服务器）、Postfix（SMTP 服务器）、Let's Encrypt（自动获取 SSL 证书）等。

6. **Web 界面**：可以通过第三方工具（如 Rainloop 或 Nextcloud）提供 Web 邮件访问。

7. **可扩展性**：用户可以根据需求扩展邮件服务器的功能，例如添加额外的插件或服务。

### 使用场景

`docker-mailserver` 适合于个人用户、小型企业或开发者，他们希望快速搭建一个可用的邮件服务器，而不想处理复杂的配置和维护工作。它可以用于处理公司内部邮件、项目邮件、或作为个人邮件服务器。

### 如何使用

要使用 `docker-mailserver`，您需要安装 Docker 和 Docker Compose。然后，您可以通过编写一个 `docker-compose.yml` 文件来配置和启动邮件服务器。官方文档提供了详细的安装和配置步骤，用户可以根据自己的需求进行调整。

### 官方资源

您可以在 GitHub 上找到 `docker-mailserver` 的官方仓库，获取更多信息和文档：
- [docker-mailserver GitHub](https://github.com/docker-mailserver/docker-mailserver)

通过这个项目，用户可以轻松地搭建和管理自己的邮件服务器，享受邮件通信的灵活性和控制权。

# 安装示例

### docker 部署

```
version: '3.3'

services:
  mailserver:
    image: ghcr.io/docker-mailserver/docker-mailserver:latest
    container_name: mailserver
    # Provide the FQDN of your mail server here (Your DNS MX record should point to this value)
    hostname: mail.dafengstudio.cn
    ports:
      - "25:25"
      - "465:465"
      - "587:587"
      - "993:993"
    volumes:
      - ./docker-data/dms/letsencrypt/:/etc/letsencrypt
      - ./docker-data/dms/mail-data/:/var/mail/
      - ./docker-data/dms/mail-state/:/var/mail-state/
      - ./docker-data/dms/mail-logs/:/var/log/mail/
      - ./docker-data/dms/config/:/tmp/docker-mailserver/
      - /etc/localtime:/etc/localtime:ro
    environment:
      - ENABLE_RSPAMD=1
      - ENABLE_CLAMAV=1
      - ENABLE_FAIL2BAN=1
      - ENABLE_POP3=1
    cap_add:
      - NET_ADMIN # For Fail2Ban to work
    restart: always
```

### dns 配置


![](attachments/Pasted%20image%2020240911211052.png)

# 添加用户

```
docker exec -it mailserver setup email add <EMAIL ADDRESS> [<PASSWORD>]


(base) [root@VM-0-13-centos projects]# docker exec -it mailserver setup email add admin@dafengstudio.cn
Enter Password: 
```


### 修改账号密码

```
docker exec -it mailserver setup email update <EMAIL ADDRESS> [<PASSWORD>]
# 比如
docker exec -it mailserver setup email update admin@domain.com "password123"
```

### 查看用户列表

```
docker exec -it mailserver setup email list
```

# 参考
1. https://wmwm.me/article/456048926181560320
2. https://www.wzhecnu.cn/2024/03/19/server/docker/docker-mailserver/