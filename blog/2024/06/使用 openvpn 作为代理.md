---
slug: openvpn-as-a-http_proxy
title: openvpn-as-a-http_proxy
authors:
  - timger
tags:
  - vpn
  - openvpn
  - proxy
---

https://github.com/jonohill/docker-openvpn-proxy/tree/master

`jonoh/openvpn-proxy`

```bash
docker stop vpn-proxy
docker rm vpn-proxy
docker run -it -d \
	--name vpn-proxy \
	--cap-add=NET_ADMIN \
	--device=/dev/net/tun \
	--dns=8.8.8.8 \
	-v ./openvpn.ovpn:/config/config.ovpn \
	-e LOCAL_NETWORK=172.31.36.60/24 \
	-p 8081:80 \
	-p 8080:8080 \
registry.dafengstudio.cn/docker-openvpn-proxy:0.0.1
docker logs -f vpn-proxy
```


本地地址 
```

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9001
        inet 172.31.36.60  netmask 255.255.240.0  broadcast 172.31.47.255
        inet6 fe80::4b7:52ff:fe08:a9bb  prefixlen 64  scopeid 0x20<link>
        ether 06:b7:52:08:a9:bb  txqueuelen 1000  (Ethernet)
        RX packets 17202302  bytes 22612215267 (21.0 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3106921  bytes 12564606672 (11.7 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

进入容器
```
docker exec -it  vpn-proxy /bin/sh

```

使用代理

```
export http_proxy=http://127.0.0.1:8080
export https_proxy=http://127.0.0.1:8080
curl -v https://google.com
```

查看日志
```bash
docker logs -f vpn-proxy
```

查看日志

```
2024-06-20 04:47:00 ERROR: Failed to apply push options
2024-06-20 04:47:00 Failed to open tun/tap interface
2024-06-20 04:47:00 SIGUSR1[soft,process-push-msg-failed] received, process restarting
2024-06-20 04:49:40 WARNING: No server certificate verification method has been enabled.  See http://openvpn.net/howto.html#mitm for more info.
2024-06-20 04:49:40 TCP/UDP: Preserving recently used remote address: [AF_INET]44.224.121.133:443
2024-06-20 04:49:40 Attempting to establish TCP connection with [AF_INET]44.224.121.133:443 [nonblock]
2024-06-20 04:49:40 TCP connection established with [AF_INET]44.224.121.133:443
2024-06-20 04:49:40 TCP_CLIENT link local: (not bound)
2024-06-20 04:49:40 TCP_CLIENT link remote: [AF_INET]44.224.121.133:443
2024-06-20 04:49:41 [server] Peer Connection Initiated with [AF_INET]44.224.121.133:443
2024-06-20 04:49:43 OPTIONS ERROR: failed to negotiate cipher with server.  Add the server's cipher ('BF-CBC') to --data-ciphers (currently 'AES-256-GCM:AES-128-GCM') if you want to connect to this server.
2024-06-20 04:49:43 ERROR: Failed to apply push options
2024-06-20 04:49:43 Failed to open tun/tap interface
2024-06-20 04:49:43 SIGUSR1[soft,process-push-msg-failed] received, process restarting
```

通过`curl`测试成功是否
```
[ec2-user@ip-172-31-36-60 ~]$ curl -v https://google.com
* Uses proxy env variable https_proxy == 'https://127.0.0.1:8080'
*   Trying 127.0.0.1:8080...
* Connected to 127.0.0.1 (127.0.0.1) port 8080 (#0)
* ALPN, offering http/1.1
*  CAfile: /etc/pki/tls/certs/ca-bundle.crt
* TLSv1.0 (OUT), TLS header, Certificate Status (22):
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
```


上面的 openvpn 版本有问题 
我自己 改了 一个版本
https://github.com/foldspace-stack/docker-openvpn-proxy

