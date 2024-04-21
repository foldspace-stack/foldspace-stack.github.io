### 实现原理

在Java中，`TreeMap`是基于红黑树的`NavigableMap`实现。红黑树是一种自平衡的二叉搜索树，它通过在节点中引入一个额外的属性——颜色（红色或黑色），来保持树的平衡。这种平衡是通过旋转和重新着色操作来维护的，确保了以下性质：

1. 每个节点要么是红色，要么是黑色。
2. 根节点是黑色。
3. 所有叶子节点（NIL节点，空节点）是黑色。
4. 如果一个节点是红色的，则它的两个子节点都是黑色的（不会有两个连续的红色节点）。
5. 从任一节点到其每个叶子节点的所有路径都包含相同数量的黑色节点。

由于这些性质，红黑树可以确保最长的路径不会超过最短路径的两倍，因此在最坏的情况下，操作的时间复杂度能够保持在O(log n)。

`TreeMap`利用红黑树的性质来实现键值对的有序存储。它保证了键的排序，这个排序可以是自然排序（根据键的`Comparable`接口），也可以是构造`TreeMap`时提供的`Comparator`。

### 用途

`TreeMap`在需要以下特性的场景中非常有用：

1. **有序的键值对**：`TreeMap`中的键总是有序的，无论是按自然排序还是自定义排序。这对于需要有序遍历键值对的应用非常重要。

2. **快速查找**：由于红黑树的性质，`TreeMap`提供了O(log n)时间复杂度的查找性能。

3. **范围查找和操作**：`TreeMap`实现了`NavigableMap`接口，提供了一系列的导航方法，如`firstEntry()`, `lastEntry()`, `higherEntry()`, `lowerEntry()`等，这些方法使得范围查找和操作变得简单高效。

4. **键值对的自动排序**：在`TreeMap`中，当添加或删除键值对时，它会自动维护排序顺序。

5. **子映射操作**：可以非常方便地获取`TreeMap`的子映射，例如`headMap()`, `tailMap()`, `subMap()`等方法，这些方法返回的是原映射的视图，而不是副本。

### 示例

下面是一个简单的`TreeMap`示例，展示了如何在Java中使用它：

```java
import java.util.TreeMap;

public class TreeMapExample {
    public static void main(String[] args) {
        // 创建一个 TreeMap，键按自然顺序排序
        TreeMap<Integer, String> treeMap = new TreeMap<>();

        // 添加键值对
        treeMap.put(3, "Three");
        treeMap.put(1, "One");
        treeMap.put(2, "Two");

        // 遍历键值对
        treeMap.forEach((key, value) -> System.out.println(key + " => " + value));

        // 获取并操作第一个（最小的键）和最后一个（最大的键）的条目
        System.out.println("First Entry: " + treeMap.firstEntry());
        System.out.println("Last Entry: " + treeMap.lastEntry());

        // 获取大于或等于给定键的最小键的条目
        System.out.println("Ceiling Entry for 2: " + treeMap.ceilingEntry(2));
    }
}
```

在这个例子中，整数键被添加到`TreeMap`中，并且由于整数具有自然的比较方法，它们会被自动排序。然后，我们遍历了映射，并使用了一些`NavigableMap`接口的方法来获取特定的条目。

# 区别

HashMap的底层是Array，所以HashMap在添加，查找，删除等方法上面速度会非常快。而TreeMap的底层是一个Tree结构，所以速度会比较慢。

另外HashMap因为要保存一个Array，所以会造成空间的浪费，而TreeMap只保存要保持的节点，所以占用的空间比较小。

HashMap如果出现hash冲突的话，效率会变差，不过在java 8进行TreeNode转换之后，效率有很大的提升。

TreeMap在添加和删除节点的时候会进行重排序，会对性能有所影响。

# 参考

1. https://www.liaoxuefeng.com/wiki/1252599548343744/1265117109276544
2. https://www.jianshu.com/p/2dcff3634326
3. https://www.cnblogs.com/flydean/p/hashmap-vs-treemap.html
4. 