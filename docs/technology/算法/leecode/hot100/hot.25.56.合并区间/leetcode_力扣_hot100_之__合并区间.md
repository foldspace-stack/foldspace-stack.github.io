# 题目

https://leetcode.cn/problems/merge-intervals?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj

![](attachments/Pasted%20image%2020240305132343.png)

# 解题

题目描述：给定一个区间的集合，合并所有重叠的区间。

举个例子，
```
假设输入的区间集合是[[1,3],[2,6],[8,10],[15,18]]，这些区间可以合并为[[1,6],[8,10],[15,18]]，因为[1,3]和[2,6]重叠了，所以合并为[1,6]。
```


解题思路：
1. 首先按照区间的起始位置进行排序，这样可以保证重叠的区间都挨在一起。
2. 然后遍历排序后的区间集合，用一个新的集合来存储合并后的结果。遍历过程中，比较当前区间与结果集合中最后一个区间的关系：
   - 如果当前区间的起始位置大于结果集合中最后一个区间的结束位置，说明它们不重叠，直接将当前区间加入结果集合。
   - 如果当前区间的起始位置小于等于结果集合中最后一个区间的结束位置，说明它们重叠，更新结果集合中最后一个区间的结束位置为当前区间的结束位置。
3. 遍历完成后，结果集合中存储的就是合并后的区间集合。

这就是题目的大致意思和解题思路，希望能帮助你理解。如果还有疑问，欢迎继续提问。


```python
from typing import *


def solution(intervals: List[List[int]]):
    new_arr = sorted(intervals, key=lambda x: x[0])
    rst = []
    range_stack = []
    for i in range(len(new_arr)):
        """
        i == 0:
            时候
            
        i:
            
        i == last:
            aa
        """
        if i == 0:
            range_stack.append(new_arr[i][0])
            range_stack.append(new_arr[i][1])
        else:
            if len(range_stack) > 0:
                if range_stack[-1] >= new_arr[i][0]:
                    """
                    合并区间
                    [[1,3],[2,6],[8,10],[15,18]]
                    """
                    if range_stack[-1] < new_arr[i][-1]:
                        range_stack.pop()
                        range_stack.append(new_arr[i][-1])
                else:
                    """
                    区间无法合并
                    """
                    rst.append([range_stack[0], range_stack[-1]])
                    range_stack.pop()
                    range_stack.pop()
                    range_stack.append(new_arr[i][0])
                    range_stack.append(new_arr[i][-1])
            else:
                """
                上一次合并完毕已经加入了区间
                """
                range_stack.append(new_arr[i][0])
                range_stack.append(new_arr[i][-1])
    rst.append([range_stack[0], range_stack[-1]])
    return rst


if __name__ == '__main__':
    print(solution([[1, 3], [2, 6], [8, 10], [15, 18]]
                   ))

```