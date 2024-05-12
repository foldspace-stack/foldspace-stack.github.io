
## 下载安装


下载 docker
https://hub.docker.com/r/sapse/abap-platform-trial/tags


```
docker pull sapse/abap-platform-trial:1909_SP01
```

镜像大约  `20.95G`  左右
## 运行

```
docker run \
	--stop-timeout 3600 \
	-i --name a4h \
	-h vhcala4hci \
	-p 3200:3200 \
	-p 3300:3300 \
	-p 8443:8443 \
	-p 30213:30213 \
	-p 50000:50000 \
	-p 50001:50001 \
	sapse/abap-platform-trial:1909_SP01 \
	-skip-limits-check
```

启动日志:

```txt
➜  ~ docker run \
        --stop-timeout 3600 \
        -i --name a4h \
        -h vhcala4hci \
        -p 3200:3200 \
        -p 3300:3300 \
        -p 8443:8443 \
        -p 30213:30213 \
        -p 50000:50000 \
        -p 50001:50001 \
        sapse/abap-platform-trial:1909_SP01 \
        -skip-limits-check
WARNING: the following system limits are below recommended values:
  (sysctl kernel.shmmni = 4096) < 32768
  (sysctl vm.max_map_count = 262144) < 2147483647
  (sysctl fs.aio-max-nr = 1048576) < 18446744073709551615
Hint: consider adding these parameters to your docker run command:
  --sysctl kernel.shmmni=32768
Hint: if you are on Linux, consider running the following system commands:
  sudo sysctl vm.max_map_count=2147483647
  sudo sysctl fs.aio-max-nr=18446744073709551615

The SAP Developer Center Software Developer License Agreement has been accepted
because the file /agree_to_SAP_license exists
You can read the license text in the file /SAP_COMMUNITY_DEVELOPER_License
in the image.
Hint: docker exec -it a4h less /SAP_COMMUNITY_DEVELOPER_License

The file /agree_to_SAP_license exists because either you restarted a container,
or you created the file manually, or you committed the file to your private image.
If you no longer agree to SAP Developer Center Software Developer License Agreenement,
please remove the file /agree_to_SAP_license from your container or image.
Hint: docker exec -it a4h rm /agree_to_SAP_license

sapinit: starting
start hostcontrol using profile /usr/sap/hostctrl/exe/host_profile
Impromptu CCC initialization by 'rscpCInit'.
  See SAP note 1266393.
Impromptu CCC initialization by 'rscpCInit'.
  See SAP note 1266393.
sapinit: started, pid=13

HDB: starting
Got unhandled signal: 28
Got unhandled signal: 28
```

启动不成功


```
Hint: Container must have at least 16GB RAM available
Hint: Container must have at least 70GB DISK free
```
访问

修改 docker 内存
![](attachments/Pasted%20image%2020240511174758.png)

