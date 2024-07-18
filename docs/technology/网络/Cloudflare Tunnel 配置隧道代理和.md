# 简介

Cloudflare Tunnel 是由 Cloudflare 提供的一种工具，用于将您的本地服务器或应用程序安全地连接到 Cloudflare 的全球网络。通过 Cloudflare Tunnel，您可以将内部部署的服务暴露到公共互联网，同时保持安全性和隐私性。

Cloudflare Tunnel 的工作原理是通过一个客户端软件（Cloudflare Warp）将您的服务器与 Cloudflare 的边缘网络连接起来。这样，您的服务器就可以通过 Cloudflare 的全球网络进行访问，获得更快的响应速度、更好的安全性和可靠性。

Cloudflare Tunnel 可以帮助您轻松地将内部服务暴露到外部网络，而无需公开暴露服务器的真实 IP 地址。这对于需要远程访问内部服务或需要在公共网络上提供服务的情况非常有用。


# 配置文件

```bash
touch ~/.cloudflared/config.yml
```

查看列表

```bash
[root@iZbp151w0p64xb817m4auqZ ~]# cloudflared tunnel list
2024-07-12T13:51:56Z ERR Configuration file /root/.cloudflared/config.yml was empty
You can obtain more detailed information for each tunnel with `cloudflared tunnel info <name/uuid>`
ID                                   NAME                          CREATED              CONNECTIONS
be525304-11121-47cb-221-221 dafengstudio-all-node-forward 2024-07-12T12:48:24Z 1xsjc05, 2xsjc06, 1xsjc08
```

配置文件

参考这里 https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/configure-tunnels/local-management/configuration-file/

```yaml
tunnel: xxxxxx

credentials-file: /root/.cloudflared/xxxxxxx.json

  

warp-routing:

enabled: true

  

ingress:

- hostname: "*.dafengstudio.cn"

service: http://172.23.32.50:80

- hostname: "*"

service: "http://172.23.32.50:80"
```

然后 

```bash
cloudflared tunnel ingress validate
```

使生效

```bash
cloudflared tunnel route dns be525304-a989-47cb-b2c7-285432cca941 *.dafengstudio.cn

```

# 参考
1. 