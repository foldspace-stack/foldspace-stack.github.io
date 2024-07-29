---
slug: qdrant 安装和部署
title: qdrant 安装和部署
date: 2024-07-24T13:00:00
authors:
  - timger
tags:
  - k8s
  - qdrant
---
# 简介

Qdrant是一个开源的向量数据库，专门用于存储和检索高维向量数据。它提供了一种高效的方式来处理大规模的向量数据，例如图像、文本、音频等。以下是Qdrant的一些功能和特性：

1. **高维向量存储**：Qdrant专注于存储和检索高维向量数据，能够有效地处理数百甚至数千维的向量。
    
2. **相似度搜索**：Qdrant支持根据向量之间的相似度进行搜索和检索，可以快速找到与查询向量最相近的向量。
    
3. **多种索引算法**：Qdrant支持多种索引算法，包括HNSW（Hierarchical Navigable Small World）和FAISS（Facebook AI Similarity Search）等，以提高检索效率。
    
4. **分布式存储**：Qdrant可以在分布式环境中部署，支持数据的分片和复制，以提高系统的可扩展性和容错性。
    
5. **RESTful API**：Qdrant提供了基于RESTful API的接口，使用户可以方便地与数据库进行交互和管理。
    
6. **灵活的配置选项**：Qdrant提供了丰富的配置选项，用户可以根据自己的需求进行调整和优化。
    
7. **开源和可扩展**：Qdrant是一个开源项目，用户可以根据自己的需求对其进行定制和扩展。
# 安装使用

https://qdrant.tech/documentation/guides/installation/

```bash
docker run -it -d \
    --name qdrant \
    -p 6333:6333 \
    -p 6334:6334 \
    -v ./qdrant_data:/qdrant/storage \
    qdrant/qdrant
```

访问

http://127.0.0.1:6333/dashboard

![](attachments/Pasted%20image%2020240725012943.png)

# 功能

以下是一个简单的Python示例，演示如何使用Qdrant加载文档数据并进行相似度搜索以及Range搜索：

```python
import requests

# 定义Qdrant的API地址
QDRANT_API_URL = 'http://localhost:6333'

# 加载文档数据
def load_documents(documents):
    response = requests.post(f'{QDRANT_API_URL}/collection', json={'documents': documents})
    return response.json()

# 进行相似度搜索
def search_document(query_vector, top_k=5):
    response = requests.post(f'{QDRANT_API_URL}/search', json={'vector': query_vector, 'top': top_k})
    return response.json()

# 进行Range搜索
def range_search_document(min_range, max_range, top_k=5):
    response = requests.post(f'{QDRANT_API_URL}/search', json={'range': {'min': min_range, 'max': max_range}, 'top': top_k})
    return response.json()

# 示例文档数据
documents = [
    {'id': '1', 'vector': [0.1, 0.2, 0.3], 'text': 'Document 1'},
    {'id': '2', 'vector': [0.4, 0.5, 0.6], 'text': 'Document 2'},
    {'id': '3', 'vector': [0.7, 0.8, 0.9], 'text': 'Document 3'}
]

# 加载文档数据
load_documents(documents)

# 查询文档
query_vector = [0.2, 0.3, 0.4]
result = search_document(query_vector)

print(result)

# Range搜索文档
min_range = 0.4
max_range = 0.6
result = range_search_document(min_range, max_range)

print(result)
```

在这个示例中，我们首先定义了Qdrant的API地址，并编写了三个函数：`load_documents`用于加载文档数据，`search_document`用于进行相似度搜索，`range_search_document`用于进行Range搜索。然后我们定义了一些示例的文档数据，加载文档数据并查询一个文档的相似文档以及进行Range搜索。最后打印出搜索结果。

Qdrant是一个向量索引库，它的搜索功能是基于向量相似度的。因此，查询向量（query_vector）通常是一个数值向量，表示待搜索的文档或查询的特征。如果要将文字转换为向量进行搜索，可以使用文本嵌入模型（如Word2Vec、BERT等）将文字转换为数值向量，然后再进行搜索。在实际应用中，可以先将文字转换为向量，然后再将向量传递给Qdrant进行相似度搜索。