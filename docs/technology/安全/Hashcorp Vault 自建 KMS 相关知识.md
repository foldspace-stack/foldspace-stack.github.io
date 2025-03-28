
## 什么是KMS 和 Hashcorp Vault

KMS（Key Management Service，密钥管理服务）和 HashiCorp Vault 都是用于安全管理和保护敏感数据的工具，但它们在功能和使用场景上有一些区别。

1. **KMS（Key Management Service）**：
   - KMS 是一种云服务，由云服务提供商（如 AWS、Google Cloud、Azure 等）提供。它主要用于管理加密密钥，帮助用户加密数据、生成密钥、解密数据等操作。
   - KMS 通常用于云环境中，为云服务提供加密和密钥管理功能。用户可以使用 KMS 来加密云存储中的数据、保护云服务中的敏感信息等。
   - KMS 一般提供了简单的 API 接口，用户可以通过调用 API 来进行密钥管理操作。

2. **HashiCorp Vault**：
   - HashiCorp Vault 是一个开源工具，用于安全地存储和管理敏感数据，如密码、API 密钥、证书等。Vault 提供了密钥管理、访问控制、加密解密、动态凭据生成、安全审计等功能。
   - Vault 可以部署在任何环境中，包括云环境和本地数据中心。它支持多种存储后端，如 Consul、MySQL、PostgreSQL 等，以及多种身份验证方法，如 LDAP、AWS IAM、GitHub 等。
   - Vault 的功能非常灵活，可以用于保护各种类型的敏感数据，并提供了丰富的安全功能，如动态凭据生成、凭据轮转、审计监控等。

虽然 KMS 和 HashiCorp Vault 都是用于密钥和敏感数据管理的工具，但它们的定位和功能有所不同。KMS 更适用于云环境中对密钥进行简单管理和加密操作，而 Vault 则提供了更为全面和灵活的安全解决方案，适用于各种环境和复杂的安全需求。在选择使用时，可以根据具体的需求和场景来决定使用哪种工具或者结合两者来增强安全性。
aaaaa

Hashcorp Vault 本身提供非常丰富的功能

![](attachments/Pasted%20image%2020240601223208.png)

## 存储引擎

https://developer.hashicorp.com/vault/docs/configuration/storage


![](attachments/Pasted%20image%2020240601213014.png)

## Secrets Engine

在 HashiCorp Vault 中，Secrets Engine 是用于管理和存储敏感数据（如密码、API 密钥、证书等）的模块。KV（Key-Value） Secrets Engine 是 Vault 中的一种特定类型的 Secrets Engine，它允许用户存储和检索以键值对形式存储的秘密数据。

![](attachments/Pasted%20image%2020240601210034.png)

### KV

KV Secrets Engine 的应用场景包括但不限于：

1. 存储密码和凭据：可以将密码、API 密钥、数据库凭据等敏感数据存储在 KV Secrets Engine 中，以便应用程序在需要时安全地检索和使用这些凭据。
    
2. 配置管理：可以将应用程序的配置信息（如连接字符串、环境变量等）存储在 KV Secrets Engine 中，确保配置信息的安全性和可管理性。
    
3. 证书管理：KV Secrets Engine 也可以用于存储和管理 TLS 证书、SSH 密钥等安全证书，帮助用户简化证书管理流程并提高安全性。
    
4. 加密数据：除了存储明文数据外，KV Secrets Engine 还可以用于加密敏感数据，确保数据在存储和传输过程中得到保护。

### PKI Certificates

在 HashiCorp Vault 中，PKI Certificates Secrets Engine 是一种用于管理和颁发公钥基础设施（PKI）证书的 Secrets Engine。PKI 是一种广泛应用于网络安全领域的加密技术，用于建立和维护安全的通信连接。

PKI Certificates Secrets Engine 的主要作用是为应用程序、服务和用户颁发和管理数字证书，以确保通信的安全性和可信性。以下是一些 PKI Certificates Secrets Engine 的应用场景：

1. TLS/SSL 证书管理：PKI Certificates Secrets Engine 可用于颁发和管理用于 HTTPS 连接的 TLS/SSL 证书，帮助用户轻松管理和更新证书，确保网站和应用程序的安全通信。

2. 服务认证：通过 PKI Certificates Secrets Engine，可以为服务颁发数字证书，用于服务之间的认证和安全通信，确保只有授权的服务可以相互通信。

3. 客户端认证：PKI Certificates Secrets Engine 还可以用于为客户端颁发数字证书，用于客户端与服务端之间的双向认证，确保双方的身份验证和通信安全。

4. 身份验证和授权：PKI Certificates Secrets Engine 可以作为身份验证和授权系统的一部分，帮助用户实现对用户、服务和设备的身份验证和授权管理。



### transit

在 HashiCorp Vault 中，Transit Secrets Engine 是一种用于加密和解密数据的服务。Transit Secrets Engine 提供了一种简单且高度可扩展的方式来对数据进行加密，同时还支持数据签名、验证和加密密钥的轮换等功能。

Transit Secrets Engine 的主要作用是在数据传输过程中对数据进行加密和解密，帮助用户安全地处理敏感数据。以下是一些 Transit Secrets Engine 的应用场景：

1. 数据加密：通过 Transit Secrets Engine，用户可以对敏感数据进行加密，确保数据在存储和传输过程中的安全性，防止数据泄露和篡改。

2. 数据解密：Transit Secrets Engine 还可以用于解密已加密的数据，只有拥有相应解密权限的用户或应用程序才能解密数据，确保数据的安全访问。

3. 数据签名和验证：Transit Secrets Engine 支持对数据进行签名和验证，帮助用户验证数据的完整性和真实性，防止数据被篡改或伪造。

4. 加密密钥管理：Transit Secrets Engine 还可以用于管理加密密钥，包括生成、轮换和撤销加密密钥，确保数据加密的安全性和可靠性。


### SSH

在 HashiCorp Vault 中，SSH Secrets Engine 是一种用于管理和自动化 SSH 认证的服务。通过 SSH Secrets Engine，用户可以动态生成和管理 SSH 密钥对，并将其用于安全地进行远程登录和身份验证。

以下是一些 SSH Secrets Engine 的应用场景：

1. 动态 SSH 密钥管理：SSH Secrets Engine 允许用户动态生成 SSH 密钥对，并自动将公钥配置到目标主机上，从而简化 SSH 密钥的管理和轮换过程。

2. 临时 SSH 访问：用户可以使用 SSH Secrets Engine 生成临时的 SSH 密钥对，用于临时性的远程登录和访问控制，确保访问权限的安全性和可控性。

3. SSH 密钥轮换：SSH Secrets Engine 支持自动化 SSH 密钥的轮换和更新，帮助用户避免长期使用相同的密钥对导致的安全风险。

4. SSH 认证管理：通过 SSH Secrets Engine，用户可以集中管理 SSH 密钥对，并实现对 SSH 认证的集中化管理和控制，提高系统的安全性和可管理性。


### TOTP

在 HashiCorp Vault 中，TOTP（Time-Based One-Time Password）Secrets Engine 是一种用于生成和管理基于时间的一次性密码（OTP）的服务。通过 TOTP Secrets Engine，用户可以生成基于时间的一次性密码，并用于实现双因素身份验证（2FA）等安全机制。

以下是一些 TOTP Secrets Engine 的应用场景：

1. 双因素身份验证：TOTP Secrets Engine 可以用于实现双因素身份验证，用户登录时需要提供除用户名和密码外的一次性密码，提高账户的安全性。

2. 安全访问控制：通过 TOTP Secrets Engine，用户可以为特定的应用或系统生成一次性密码，用于安全地限制和控制对敏感资源的访问。

3. 临时授权：用户可以使用 TOTP Secrets Engine 生成临时的一次性密码，用于临时性的授权和访问控制，确保访问权限的安全性和时效性。

4. 密钥管理：TOTP Secrets Engine 还可以用于生成和管理加密密钥，用于数据加密和解密等安全操作。

### LDAP

在 HashiCorp Vault 中，LDAP Secrets Engine 是一种用于与 LDAP（Lightweight Directory Access Protocol）服务器集成的服务。LDAP 是一种用于访问和维护分布式目录信息服务的协议，通常用于存储和组织用户、组织架构和其他目录信息。

LDAP Secrets Engine 允许 Vault 与现有的 LDAP 目录服务进行集成，以便在应用程序和系统中安全地管理和访问 LDAP 凭据和其他目录信息。以下是一些 LDAP Secrets Engine 的应用场景：

1. 凭据管理：LDAP Secrets Engine 可以用于安全地存储和管理 LDAP 用户凭据、服务账号、证书等敏感信息，避免在应用程序中明文存储密码或凭据。

2. 动态凭据生成：LDAP Secrets Engine 支持动态生成和轮转 LDAP 凭据，提供了一种安全的方式来管理和更新凭据，减少了凭据泄露和滥用的风险。

3. 自动化身份验证：Vault 可以通过 LDAP Secrets Engine 自动化身份验证过程，帮助用户实现单点登录（SSO）、多因素身份验证等安全机制，提高系统的安全性和用户体验。

4. 访问控制：LDAP Secrets Engine 可以与 Vault 的访问控制策略结合使用，实现基于 LDAP 用户和组织架构的细粒度访问控制，确保只有授权用户可以访问敏感资源。


### Kubernetes

在 HashiCorp Vault 中，Kubernetes Secrets Engine 是一种用于与 Kubernetes 集成的服务。Kubernetes 是一种流行的容器编排平台，用于部署、扩展和管理容器化应用程序。Kubernetes Secrets Engine 允许 Vault 与 Kubernetes 集群进行集成，以便在应用程序和容器中安全地管理和访问敏感信息。

以下是一些 Kubernetes Secrets Engine 的应用场景：

1. 容器化应用程序凭据管理：Kubernetes Secrets Engine 可以用于安全地存储和管理容器化应用程序所需的敏感凭据，如数据库密码、API 密钥等。这样可以避免在容器镜像或配置文件中硬编码凭据，提高安全性。

2. 动态凭据生成：Kubernetes Secrets Engine 支持动态生成和轮转凭据，使得容器化应用程序可以动态获取最新的凭据，减少了凭据泄露和滥用的风险。

3. 自动化部署：Vault 可以与 Kubernetes Secrets Engine 结合使用，实现自动化部署过程中的凭据注入和管理，简化了容器化应用程序的部署和配置流程。

4. 访问控制：Kubernetes Secrets Engine 可以与 Kubernetes 的 RBAC（Role-Based Access Control）机制结合使用，实现基于角色的访问控制，确保只有授权的容器可以访问敏感凭据。

5. 整合 CI/CD 流水线：Kubernetes Secrets Engine 可以与 CI/CD 工具集成，实现在持续集成和持续部署过程中安全地管理和传递凭据，保护敏感信息不被泄露。

### cloud aws

在 HashiCorp Vault 中，AWS Secrets Engine 是一种用于与亚马逊 Web 服务（AWS）云平台集成的服务。AWS Secrets Engine 允许 Vault 在 AWS 环境中安全地管理和访问 AWS 凭据和密钥，并提供了一些特定的应用场景。

以下是一些 AWS Secrets Engine 的应用场景：

1. 动态凭据生成：AWS Secrets Engine 支持动态生成和轮转 AWS 凭据，如访问密钥、安全凭据等，使得应用程序可以动态获取最新的凭据，减少了凭据泄露和滥用的风险。

2. 自动化凭据管理：Vault 可以与 AWS Secrets Engine 结合使用，实现自动化的 AWS 凭据管理流程，包括凭据的创建、更新、删除等操作，简化了对 AWS 资源的访问控制。

3. 安全凭据存储：AWS Secrets Engine 可以用于安全地存储和管理 AWS 相关的敏感信息，如 API 密钥、证书、密码等，确保这些凭据不被明文存储或传输，提高了安全性。

4. 与 AWS 服务集成：AWS Secrets Engine 可以与 AWS 服务集成，实现对 AWS 资源的自动化管理和访问控制，如自动化部署、备份、监控等操作。

5. 与 DevOps 工具集成：AWS Secrets Engine 可以与 DevOps 工具集成，如 Terraform、Ansible 等，实现在 CI/CD 流水线中安全地管理和传递 AWS 凭据，保护敏感信息不被泄露。


## 场景展示

### on k8s

![](attachments/Pasted%20image%2020240601211327.png)

### KMS 和 nacos 配置中心配合使用

```puml


```
