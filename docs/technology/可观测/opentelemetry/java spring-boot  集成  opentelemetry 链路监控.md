
# 简介

OpenTelemetry 是一个开放标准，用于跟踪和监控分布式应用程序。它提供了一组跟踪和指标的规范，以及多语言库和工具，帮助开发人员在应用程序中实现跟踪和监控功能。OpenTelemetry 旨在统一和标准化跟踪数据的收集、传输和分析，使得在复杂的分布式系统中更容易实现可观测性。

所以 OpenTelemetry 类似 java 的一套标准接口，不同厂商实现自己不同的具体实现
![](attachments/Pasted%20image%2020240614180054.png)


https://cloud.tencent.com/developer/article/2096468


# 方式

## agent 方式

### 环境配置

```Dockerfile
ENV JAVA_TOOL_OPTIONS="-javaagent:/app/agent-lib/opentelemetry-javaagent.jar"  
ENV OTEL_SERVICE_NAME="wbttt-server"  
ENV OTEL_TRACES_EXPORTER="otlp"  
#ENV OTEL_METRICS_EXPORTER="none"  
#ENV OTEL_LOGS_EXPORTER="none"  
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://xxxx.temp:3100"
```

### 参数配置

```Dockerfile
CMD ["java", "-javaagent:opentelemetry-javaagent.jar", "-Dotel.resource.attributes=service.name=test-service", "-Dotel.traces.exporter=jaeger", "-Dotel.exporter.jaeger.endpoint=http://localhost:14250", "-jar", "/test-service.jar"]
```


其中很多系统配置参考 https://opentelemetry.io/docs/zero-code/java/agent/configuration/

如果大 trace

```xml
  <dependency>
    <groupId>io.opentelemetry.instrumentation</groupId>
    <artifactId>opentelemetry-instrumentation-annotations</artifactId>
    <version>2.4.0</version>
  </dependency>
```

https://opentelemetry.io/docs/zero-code/java/agent/annotations/

参考这个


1. https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/
2. https://grafana.com/docs/grafana-cloud/monitor-applications/application-observability/setup/instrument/java/production/
3. https://grafana.com/docs/tempo/latest/api_docs/ 如果健康监测 查看服务起来没
4. https://opentelemetry.io/docs/zero-code/java/agent/configuration/


## 工程集成


# 常见错误

1. otel.javaagent WARN io.opentelemetry.instrumentation.resources.ManifestResourceProvider - Error reading manifest                                                    ```


2. Failed to export spans. Server responded with HTTP status code 404. Error message: Unable to parse response body, HTTP status message: Not Found

3.  Failed to export metrics. Server responded with UNIMPLEMENTED. This usually means that your collector is not configured with an otlp receiver in the "pipelines" section of the configuration. If export is not desired and you are using OpenTelemetry autoconfiguration or the javaagent, disable export by setting OTEL_METRICS_EXPORTER=none. Full error message: unknown service opentelemetry.proto.collector.metrics.v1.MetricsService
		1. 

