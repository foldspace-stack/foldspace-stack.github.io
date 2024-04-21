# 简介


Django 的 storage 接口提供了一个统一的方式来处理文件的存储和访问，无论是在本地文件系统、远程存储（如 Amazon S3）、还是其他自定义的存储后端。通过 storage 接口，开发人员可以方便地处理文件的上传、下载、删除等操作，而无需关心文件存储的具体细节。

以下是 Django 的 storage 接口的一些关键特点和常见用法：

1. **抽象文件存储**：storage 接口提供了一个抽象层，使得开发者可以在不修改代码的情况下切换不同的存储后端，例如从本地文件系统切换到 Amazon S3。

2. **文件上传和访问**：通过 storage 接口，可以方便地处理用户上传的文件，并在需要时提供文件的访问和下载功能。

3. **静态文件处理**：在 Web 应用中，静态文件（如 CSS、JavaScript 和图像）的管理也是 storage 接口的一部分，可以通过它来处理静态文件的存储和访问。

4. **自定义存储后端**：开发人员可以编写自定义的存储后端，以满足特定的存储需求，例如将文件存储到自定义的云存储服务中。

5. **默认存储设置**：Django 允许开发者在配置文件中指定默认的存储后端，使得应用程序可以统一使用指定的存储方式，同时也可以在需要时使用其他存储后端。

如果要自定义 需要 `DEFAULT_FILE_STORAGE` 属性改掉

开源项目参见： https://github.com/py-pa/django-minio-storage

`setting` 配置如下

亲测可用：

```python
# MiniO  
#  
DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"  
STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"  
MINIO_STORAGE_ENDPOINT = 'storage.dafengstudio.cn'  
MINIO_STORAGE_ACCESS_KEY = 'your-access-key'  
MINIO_STORAGE_SECRET_KEY = 'your-secret-key'  
MINIO_STORAGE_USE_HTTPS = False  
MINIO_STORAGE_MEDIA_OBJECT_METADATA = {"Cache-Control": "max-age=1000"}  
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'df-video-cms'  
MINIO_STORAGE_MEDIA_BACKUP_BUCKET = 'df-video-cms-recycle-bin'  
MINIO_STORAGE_MEDIA_BACKUP_FORMAT = '%c/'  
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True  
MINIO_STORAGE_STATIC_BUCKET_NAME = 'df-video-cms-static'  
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True  
#  
# End MiniO  
#
```


# 参考

1. https://django-minio-storage.readthedocs.io/en/latest/usage/