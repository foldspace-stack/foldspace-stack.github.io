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

```bash
docker run -it -d \
	--name vpn-proxy \
	--cap-add=NET_ADMIN \
	-v /home/ec2-user/openvpn.ovpn:/config/config.ovpn \
	-e LOCAL_NETWORK=172.31.36.60/24 \
	-p 8080:8080 \
jonoh/openvpn-proxy
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

使用代理

```
export http_proxy=http://127.0.0.1:8080
export https_proxy=https://127.0.0.1:8080
```


