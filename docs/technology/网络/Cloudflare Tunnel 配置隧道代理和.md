

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
tunnel: be525304-a989-47cb-b2c7-285432cca941

credentials-file: /root/.cloudflared/be525304-a989-47cb-b2c7-285432cca941.json

warp-routing:
ingress:
- hostname: gitlab.widgetcorp.tech

service: http://localhost:80

- hostname: gitlab-ssh.widgetcorp.tech

service: ssh://localhost:22

- service: http_status:404
enabled: true
```