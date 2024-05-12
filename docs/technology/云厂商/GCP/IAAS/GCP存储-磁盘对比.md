
默认情况下，每个 Compute Engine 虚拟机都有一个包含操作系统的启动磁盘。启动磁盘数据通常存储在 Persistent Disk 卷上。当您的应用需要额外的存储空间时，您可以为虚拟机预配以下一个或多个存储卷。

如需详细了解每种存储方案，请参阅下表：

|  | 平衡  
Persistent Disk | SSD  
Persistent Disk | 标准  
Persistent Disk | 极端  
Persistent Disk | 平衡 Hyperdisk | Hyperdisk Extreme | Hyperdisk Throughput | 本地 SSD | Cloud Storage 存储桶 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **存储类型** | 经济实惠、可靠的块存储 | 快速、可靠的块存储 | 高效、可靠的块存储 | 最高性能的 Persistent Disk 块存储选项，IOPS 可自定义 | 满足要求苛刻的工作负载的高性能，成本更低 | 具有可自定义的 IOPS 的最快块存储选项 | 经济实惠且以吞吐量为导向的块存储，吞吐量可自定义 | 高性能本地块存储 | 经济实惠的对象存储 |
| **每个磁盘的最小容量** | 可用区级：10 GiB  
区域级：10 GiB | 可用区级：10 GiB  
区域级：10 GiB | 可用区级：10 GiB  
区域级：200 GiB | 500 GiB | 4 GiB | 64 GiB | 2 TiB | 375 GiB、3 TiB（使用 [Z3](https://cloud.google.com/compute/docs/storage-optimized-machines?hl=zh-cn#z3_series)） | 不适用 |
| **每个磁盘的最大容量** | 64 TiB | 64 TiB | 64 TiB | 64 TiB | 64 TiB | 64 TiB | 32 TiB | 375 GiB，  
3 TiB（使用 [Z3](https://cloud.google.com/compute/docs/storage-optimized-machines?hl=zh-cn#z3_series)） | 不适用 |
| **容量增量** | 1 GiB | 1 GiB | 1 GiB | 1 GiB | 1 GiB | 1 GiB | 1 GiB | 取决于机器类型[†](#fn-logical2) | 不适用 |
| **每个虚拟机的容量上限** | 257 TiB[\*](#fn-logical1) | 257 TiB[\*](#fn-logical1) | 257 TiB[\*](#fn-logical1) | 257 TiB[\*](#fn-logical1) | 512 TiB[\*](#fn-logical1) | 512 TiB[\*](#fn-logical1) | 512 TiB[\*](#fn-logical1) | 36 TiB | 几乎无限 |
| **访问范围** | 可用区 | 可用区 | 可用区 | 可用区 | 可用区 | 可用区 | 可用区 | 实例 | 全球 |
| **数据冗余** | 可用区级和多可用区级 | 可用区级和多可用区级 | 可用区级和多可用区级 | 可用区级 | 可用区级 | 可用区级 | 可用区级 | 否 | 单区域、双区域或多区域 |
| **静态加密** | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 |
| **自定义加密密钥** | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 否 | 是 |
| **操作方法** | 
*   [添加 Persistent Disk](https://cloud.google.com/compute/docs/disks/add-persistent-disk?hl=zh-cn#create_disk)
*   [添加区域级 Persistent Disk](https://cloud.google.com/compute/docs/disks/regional-persistent-disk?hl=zh-cn)

 | [添加极端 Persistent Disk](https://cloud.google.com/compute/docs/disks/add-persistent-disk?hl=zh-cn#create_disk) | [添加 Hyperdisk](https://cloud.google.com/compute/docs/disks/add-hyperdisk?hl=zh-cn) | [添加本地 SSD](https://cloud.google.com/compute/docs/disks/add-local-ssd?hl=zh-cn#create_local_ssd) | [连接存储桶](https://cloud.google.com/compute/docs/disks?hl=zh-cn#gcsbuckets) |