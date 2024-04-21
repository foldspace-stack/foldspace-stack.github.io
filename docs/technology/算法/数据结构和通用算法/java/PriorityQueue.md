
在Java中，`PriorityQueue` 是一种基于优先级堆的无界队列。它实现了 `Queue` 接口，提供了基于优先级的元素排序机制。Java的 `PriorityQueue` 默认情况下是一个最小堆，也就是说，队列头部是按照自然排序或者自定义 `Comparator` 排序的最小元素。

### 实现原理

`PriorityQueue` 的底层是一个动态数组，用来存储队列中的元素，同时保持堆的性质。当元素被插入或者删除时，`PriorityQueue` 会自动调整内部数组的顺序，以维持堆的特性。

- **插入元素**：当新元素被添加到队列中时，它首先被放在数组的末尾，然后执行上浮（或称为上滤）操作，将这个元素移动到合适的位置，以维持最小堆的性质。
- **删除元素**：通常删除的是队列头部的元素，即最小元素。删除操作会将数组末尾的元素移动到头部，然后执行下沉（或称为下滤）操作，将这个元素移动到合适的位置，以保持最小堆的性质。

### 用途

`PriorityQueue` 通常用于那些需要快速访问最小元素（或者根据自定义 `Comparator` 的最高优先级元素）的场景，比如：

- **任务调度**：在任务调度和管理中，可以使用 `PriorityQueue` 来确保优先级高的任务先执行。
- **Dijkstra算法**：在图算法中，比如Dijkstra算法，`PriorityQueue` 被用来选择下一个要访问的最短路径节点。
- **哈夫曼编码**：在构建哈夫曼编码树时，`PriorityQueue` 可以用来选择频率最小的节点合并。
- **数据流中的中位数查找**：`PriorityQueue` 可以用来维护数据流中的中位数。
- **模拟系统**：在模拟系统中，`PriorityQueue` 可以用来根据事件的预定时间排序，确保按顺序处理事件。

### 示例

下面是一个简单的 `PriorityQueue` 示例，展示了如何在Java中使用它：

```java
import java.util.PriorityQueue;

public class PriorityQueueExample {
    public static void main(String[] args) {
        // 创建一个 PriorityQueue，默认最小元素在队列头部
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        // 添加元素
        pq.add(10);
        pq.add(20);
        pq.add(15);

        // 访问队列头部元素（最小元素），但不移除
        System.out.println("Peek: " + pq.peek()); // 输出 10

        // 移除队列头部元素（最小元素）
        System.out.println("Poll: " + pq.poll()); // 输出 10

        // 再次访问队列头部元素
        System.out.println("Peek after poll: " + pq.peek()); // 输出 15
    }
}
```

在这个例子中，整数被添加到优先级队列中，每次调用 `poll()` 方法时，都会移除并返回当前队列中的最小元素。这是因为 `PriorityQueue` 默认使用自然排序，对于整数来说，就是数值的升序。如果需要改变排序方式，可以在创建 `PriorityQueue` 时提供一个自定义的 `Comparator`。

# 参考

1. https://juejin.cn/post/6859724629616164871