# 前言

我自己有一堆服务器, 之前是用腾讯云 反向代理出去

# 操作

 进入 cloudflare
 进入 zero trust
 创建 tunnels
![](attachments/Pasted%20image%2020250310141310.png)


```
vim /etc/systemd/system/foldspace-ingress.service

[Unit]
Description=foldspace ingress
After=network.target

[Service]
ExecStart=/usr/local/bin/cloudflared tunnel --name foldspace-http-web-forward tcp://192.168.31.87
Restart=on-failure

[Install]
WantedBy=multi-user.target

```

验证
```
systemctl daemon-reload
systemctl start foldspace-ingress
systemctl status foldspace-ingress
```