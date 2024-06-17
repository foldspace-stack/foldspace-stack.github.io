
# 安装 supervisord

```bash
yum install wget vim curl
wget https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/Packages/s/supervisor-4.2.2-3.el9.noarch.rpm
dnf -y install supervisor-4.2.2-3.el9.noarch.rpm
systemctl restart supervisord
systemctl enable supervisord
```

另外也有 docker 方式安装 不是官方推荐，自己网上搜

# 编写 supervisord文件

`/etc/supervisord.d/github-ci-runner.ini`

内容如下

```ini
[program:github-ci]
command=/home/ec2-user/actions-runner/run.sh
directory=/home/ec2-user/actions-runner
autostart=true
autorestart=true
user=ec2-user
stderr_logfile=/var/log/github-ci.err.log
stdout_logfile=/var/log/github-ci.out.log
environment=ENV_VAR1="value1",ENV_VAR2="value2"
```

更新组 

```bash
[root@ip-172-31-36-60 actions-runner]# supervisorctl update
github-ci: added process group
[root@ip-172-31-36-60 actions-runner]#
```

如果要配置 共用的 token 相关就直接配置在 `environment` 变量中

如果需要项目级别的 共享的 github ci action runner

https://github.com/organizations/dafengstudio/settings/actions/runners

替换上面的项目名

然后

![](attachments/Pasted%20image%2020240602205748.png)

就 ok
