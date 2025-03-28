# 简介

APITable 的详细介绍，结合其核心功能、技术架构、应用场景及开源特性进行说明：

APITable 是一款开源的多维表格与可视化数据库工具，由 vika维格表 的社区版发展而来。其定位为 零代码/低代码平台，旨在通过直观的表格界面和强大的 API 支持，降低数据管理与应用开发的门槛。核心功能包括：56

多维表格与视图：支持表格视图、看板视图、甘特图、日历视图、相册视图等，满足不同场景的数据展示需求。

实时协作：允许多用户同时编辑同一表格，支持 OT（Operational Transformation）算法确保数据一致性。

一键生成 API：通过内置的 API 面板，用户无需编码即可将数据表快速转化为 RESTful API，便于与其他系统集成。

自动化与扩展性：支持自定义公式、机器人自动化（如与 n8n、Zapier 集成）、BI 数据看板等，用户可灵活扩展功能。

企业级特性：提供团队权限管理、单点登录（SSO）、数据备份与审计日志等功能，适用于中大型组织。


##  典型应用场景
APITable 适用于多种业务场景，尤其适合非技术人员快速构建轻量级应用：68

项目管理：通过甘特图跟踪任务进度，利用看板视图管理敏捷开发流程。

客户关系管理（CRM）：自定义字段记录客户信息，结合自动化机器人触发邮件或消息提醒。

数据可视化：将原始数据转化为交互式 BI 看板，支持动态图表与实时数据更新。

API 快速开发：作为后端服务的替代方案，快速生成 API 供小程序、Web 应用调用。

但是开源版本存在限制
# 如何突破限制

```
backend-server/application/src/main/java/com/apitable/interfaces/billing/model/DefaultSubscriptionFeature.java
```
进入代码 都改大

```java
    @Override
    public RowsPerSheet getRowsPerSheet() {
        return new RowsPerSheet(1000 * 100L);
    }

    @Override
    public ArchivedRowsPerSheet getArchivedRowsPerSheet() {
        return new ArchivedRowsPerSheet(250 * 1000 * 1000L);
    }

    @Override
    public TotalRows getTotalRows() {
        return new TotalRows(1000 * 1000 * 250000L);
    }
    
```

# 然后执行 构建任务


```shell
make _build-java
```

> 需要java17 版本

最后找到构建完的jar

```txt
➜  apitable git:(develop) ✗ find . -name "*.jar"
./init-db/gradle/wrapper/gradle-wrapper.jar
./backend-server/shared/core/build/libs/core.jar
./backend-server/shared/starters/sms/build/libs/sms.jar
./backend-server/shared/starters/mail/build/libs/mail.jar
./backend-server/shared/starters/amqp/build/libs/amqp.jar
./backend-server/shared/starters/socketio/build/libs/socketio.jar
./backend-server/shared/starters/oss/build/libs/oss.jar
./backend-server/shared/starters/beetl/build/libs/beetl.jar
./backend-server/shared/starters/databus/build/libs/databus.jar
./backend-server/gradle/wrapper/gradle-wrapper.jar
./backend-server/buildSrc/build/libs/buildSrc.jar
./backend-server/application/build/libs/application.jar
➜  apitable git:(develop) ✗ ls -alh ./backend-server/application/build/libs/application.jar
-rw-r--r--  1 timger  staff   183M Mar 28 21:14 ./backend-server/application/build/libs/application.jar

```

和线上对比
```
bash-4.2# ls -alh 
total 183M
drwxr-xr-x 1 root root 4.0K Mar 24 17:11 .
drwxr-xr-x 1 root root 4.0K Mar 24 17:10 ..
-rw-r--r-- 1 root root 183M Dec 30 19:02 app.jar
drwxr-xr-x 3 root root 4.0K Mar 28 19:28 logs
bash-4.2# 

```

和线上版本文件大小就是他

# docker 容器替换


```
/app/app.jar
```

修改docker-compose

```
  backend-server:
    image: ${IMAGE_REGISTRY}/${IMAGE_BACKEND_SERVER}
    pull_policy: ${IMAGE_PULL_POLICY:-if_not_present}
    restart: always
    env_file:
      - "${ENV_FILE:-.env}"
    expose:
      - "8081"
    environment:
      - TZ=${TIMEZONE}
      - DEFAULT_TIME_ZONE=${TIMEZONE}
    volumes:
      - ./backend-server/application/build/libs/application.jar:/app/app.jar
    networks:
      - apitable
    depends_on:
      init-db:
        condition: service_completed_successfully
```

更新
```shell
docker-compose up -d
```

