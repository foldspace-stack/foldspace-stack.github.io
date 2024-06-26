---
slug: Azure-OpenAI-API-限流问题
title: Azure OpenAI API 限流问题
authors:
  - timger
tags:
  - python
  - sse
  - azure
---
关于配额的文档

https://learn.microsoft.com/zh-cn/azure/ai-services/openai/how-to/quota?tabs=rest

相关指标

| 指标 | 解释 |
| ---- | ---- |
| RPM (requests per minute) | 每分钟请求次数 |
| RPD (requests per day) | 每天请求次数 |
| TPM (tokens per minute) | 每分钟 Token 数 |
| TPD (tokens per day), | 每天 Token 数 |

参考
1. https://learn.microsoft.com/zh-cn/azure/ai-services/openai/how-to/quota?tabs=rest
2. https://learn.microsoft.com/zh-cn/azure/ai-services/openai/quotas-limits
3. https://cloud.tencent.com/developer/article/2367426
4. https://learn.microsoft.com/zh-cn/azure/ai-services/openai/how-to/dynamic-quota
5. 