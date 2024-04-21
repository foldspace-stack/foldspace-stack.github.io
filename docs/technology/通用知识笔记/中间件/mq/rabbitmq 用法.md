
测试地址

http://192.168.31.60:15672/#/


```bash
 pip3 install pika
```



## **AMQP 是什么?**

AMQP（Advanced Message Queuing Protocol）是一种用于应用程序之间进行消息通信的开放标准协议，RabbitMQ 就是 AMQP 协议的 Erlang 的实现。

一些关键的AMQP概念包括：

1. **生产者（Producer）：** 生成并发送消息的应用程序。
2. **消费者（Consumer）：** 接收并处理消息的应用程序。
3. **Exchange（交换机）：** 用于接收生产者发送的消息，并将其路由到一个或多个队列。
4. **Queue（队列）：** 存储消息的地方，消费者从队列中获取消息进行处理。
5. **Binding（绑定）：** 定义了交换机和队列之间的关系，规定了如何将消息从交换机路由到队列。
6. **Broker（代理）：** 实现AMQP协议的消息中间件，负责接收、存储、路由和传递消息。

# 参考
1. https://juejin.cn/post/6844904125935665160
2. https://mikechen.cc/17349.html