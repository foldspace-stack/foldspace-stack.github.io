---
slug: playwright-代理相关
title: playwright-代理相关
date: 2024-07-29T13:00:00
authors:
  - timger
tags:
  - langchain
  - langflow
---
## 调用自己函数

https://github.com/langflow-ai/langflow/discussions/1272



# 错误

### Fernet key must be 32 url-safe base64-encoded bytes.


https://github.com/langflow-ai/langflow/discussions/1521

在这里生成, 更新环境变量

```yaml
- name: "LANGFLOW_SECRET_KEY"
value: "xxxxx="
```

然后 重新部署

##  json format 时候

```
'messages' must contain theword 'json' in some form, to use                'response_format' of type 'json_object
```

提示词 需要包含 

```python
import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-03-01-preview"
)

response = client.chat.completions.create(
  model="gpt-4-0125-Preview", # Model = should match the deployment name you chose for your 0125-Preview model deployment
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
print(response.choices[0].message.content)
```

### `"Error building Component OpenAI:\n\nExpected mapping type as input to ChatPromptTemplate. Received <class 'list'>`

这个错误提示表明在构建 OpenAI 组件时，ChatPromptTemplate 预期接收一个映射类型（mapping type，如字典），但实际上接收到了一个列表（list）。这种类型不匹配导致了错误。

要解决这个问题，您可以检查代码中传递给 ChatPromptTemplate 的参数，确保传递的是一个字典而不是列表。您可以通过以下步骤来调整代码：

1. 确保传递给 ChatPromptTemplate 的参数是一个字典，例如：
```python
prompt_template = {
    "key1": "value1",
    "key2": "value2"
}
```

2. 将这个字典作为参数传递给 ChatPromptTemplate，而不是一个列表：
```python
chat_prompt_template = ChatPromptTemplate(prompt_template)
```

通过以上步骤，您可以修复这个错误，并确保 ChatPromptTemplate 正确接收到预期的输入类型。如果还有其他问题或需要进一步帮助，请随时告诉我！

### `Error building Component OpenAI:\n\ndictionary update sequence element #0 has length 1; 2 is required`

