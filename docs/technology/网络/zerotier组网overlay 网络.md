
ZeroTier是一个开源的软件定义的广域网（SD-WAN）工具，可以让用户轻松地创建和管理虚拟专用网络（VPN）。ZeroTier的目标是提供简单、安全和高效的网络连接解决方案，无论是用于个人使用还是企业级网络。

使用ZeroTier，用户可以将多个设备连接在一个虚拟的专用网络中，实现设备之间的安全通信和数据传输。ZeroTier的特点包括简单易用的配置、数据加密保护、跨平台支持、多设备连接、自动路由和流量优化等功能。

ZeroTier的工作原理是通过创建一个全球性的虚拟网络，让用户的设备可以直接连接到这个网络，实现设备之间的直接通信，而无需通过传统的互联网路由器。这样可以实现更快速、更安全的数据传输，同时也可以绕过地理位置和网络限制，让用户在任何地方都能轻松访问他们的设备和数据。

https://www.zerotier.com/

# 命令简介

1. `zerotier-cli`：`zerotier-cli` 是 ZeroTier 的命令行控制工具，用于管理 ZeroTier 虚拟网络。通过 `zerotier-cli`，您可以执行各种操作，如创建网络、添加/删除成员、查看网络状态等。这个工具提供了丰富的命令选项，使您可以方便地进行网络管理和配置。
    
2. `zerotier-idtool`：`zerotier-idtool` 是用于生成和管理 ZeroTier 身份证书和密钥的工具。在 ZeroTier 中，每个节点都有一个唯一的身份证书和密钥对，用于身份验证和加密通信。`zerotier-idtool` 可以用来生成这些证书和密钥，以便节点可以安全地加入 ZeroTier 网络。
    
3. `zerotier-one`：`zerotier-one` 是 ZeroTier 的主要客户端程序，用于在节点上运行 ZeroTier 虚拟网络。`zerotier-one` 负责处理节点的网络连接、数据传输和加密通信等任务。通过 `zerotier-one`，节点可以加入 ZeroTier 网络，并与其他节点进行通信。
```

# 家庭网络加入 zerotier

# 配置加速中继

```bash
curl -s https://install.zerotier.com/ | sudo bash
```

加入网络

```bash
zerotier-cli join xxxxxxxx
```

查看加入
```
[root@iZbp151w0p64xb817m4auqZ ~]# zerotier-cli listnetworks
200 listnetworks <nwid> <name> <mac> <status> <type> <dev> <ZT assigned ips>
200 listnetworks xxxx dafengstudio-office fe:0b:dc:26:f4:c0 OK PRIVATE  xxxxx 172.23.59.63/16
```

查看进城状态

```bash
[root@iZbp151w0p64xb817m4auqZ ~]# service zerotier-one status
Redirecting to /bin/systemctl status zerotier-one.service
● zerotier-one.service - ZeroTier One
   Loaded: loaded (/usr/lib/systemd/system/zerotier-one.service; enabled; vendor preset: disabled)
   Active: active (running) since Sat 2024-07-06 17:19:00 CST; 19min ago
 Main PID: 7810 (zerotier-one)
    Tasks: 25
   Memory: 14.8M
   CGroup: /system.slice/zerotier-one.service
           └─7810 /usr/sbin/zerotier-one

Jul 06 17:19:00 iZbp151w0p64xb817m4auqZ systemd[1]: Started ZeroTier One.
Jul 06 17:19:00 iZbp151w0p64xb817m4auqZ zerotier-one[7810]: Starting Control Plane...
Jul 06 17:19:00 iZbp151w0p64xb817m4auqZ zerotier-one[7810]: Starting V6 Control Plane...

```


![](attachments/Pasted%20image%2020240706180105.png)

查看连接 

```txt
[root@iZbp151w0p64xb817m4auqZ zerotier-one]# zerotier-cli listpeers
200 listpeers <ztaddr> <path> <latency> <version> <role>
200 listpeers 62f865ae71 50.7.252.138/9993;41764;22562 796 - PLANET
200 listpeers 778cde7190 103.195.103.66/9993;41764;86593 210 - PLANET
200 listpeers cafe04eba9 - -1 - PLANET
200 listpeers cafe9efeb9 104.194.8.134/9993;1725;11852 155 - PLANET
200 listpeers cf86f8157d - -1 1.14.0 LEAF
200 listpeers d779edf763 - -1 - LEAF
200 listpeers fada62b015 35.209.252.68/61370;21389;21389 199 1.14.0 LEAF
```


这个显示是通过 ZeroTier CLI 命令 `zerotier-cli listpeers` 获取的关于当前 ZeroTier 网络中节点的信息。每行显示一个节点的信息，包括节点的 ZeroTier 地址、连接路径、延迟、版本和角色。

- `<ztaddr>`：节点的 ZeroTier 地址。
- `<path>`：节点的连接路径，包括 IP 地址/端口；如果是 Leaf 节点，则可能显示 `-`。
- `<latency>`：节点之间的延迟，单位为毫秒。
- `<version>`：节点的 ZeroTier 版本号。
- `<role>`：节点的角色，可以是 PLANET（中心节点）或 LEAF（叶节点）。

根据您提供的信息，大多数节点的信息看起来正常，没有异常指标。延迟（latency）的值通常越低越好，但也取决于网络状况和节点之间的距离。其中有一个节点的连接路径显示为 `-`，这可能表示该节点是一个 Leaf 节点，无法直接连接到其他节点。


# 手机端使用

手机安装

# 参考
1. https://www.daweibro.com/node/263
2. https://developer.aliyun.com/article/1046697
3. https://fast.v2ex.com/t/950148
4. https://zhuanlan.zhihu.com/p/573746661
5. https://www.v2ex.com/t/869846