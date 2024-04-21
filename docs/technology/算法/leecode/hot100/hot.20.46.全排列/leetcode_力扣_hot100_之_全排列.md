
# 题目

https://leetcode.cn/problems/permutations/?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj


![[Pasted image 20240305105549.png]]

#  解题

排列问题 基本就是回溯法

```python
from typing import *


def solution(nums: List[int]):
    """
    回溯法
    路径 
    """
    rst = []
    length = len(nums)
    visited = [False for i in range(length)]

    def backtrack(path, chooice_list):
        """
        位置为 i 时候的排列情况
        """
        if len(path) >= len(chooice_list):
            rst.append(path[:])
            return
        for i in range(len(chooice_list)):
            if not visited[i]:
                visited[i] = True
                path.append(nums[i])
                backtrack(path,chooice_list)
                path.pop()
                visited[i] = False

    backtrack([],nums)
    return rst

```


执行的顺序逻辑如下：


```txt
permute([1, 2, 3])
|
|--backtrack([])
|  |
|  |--choose 1
|  |  |
|  |  |--backtrack([1])
|  |  |  |
|  |  |  |--choose 2
|  |  |  |  |
|  |  |  |  |--backtrack([1, 2])
|  |  |  |  |  |
|  |  |  |  |  |--choose 3
|  |  |  |  |  |  |
|  |  |  |  |  |  |--backtrack([1, 2, 3]) - Add [1, 2, 3] to result
|  |  |  |  |  |  |
|  |  |  |  |  |  |--backtrack([1, 2]) - Pop 3, mark 3 as unvisited
|  |  |  |  |  |
|  |  |  |  |  |--choose 3 (already visited, skip)
|  |  |  |  |
|  |  |  |  |--backtrack([1]) - Pop 2, mark 2 as unvisited
|  |  |  |
|  |  |  |--choose 3
|  |  |  |  |
|  |  |  |  |--backtrack([1, 3])
|  |  |  |  |  |
|  |  |  |  |  |--choose 2
|  |  |  |  |  |  |
|  |  |  |  |  |  |--backtrack([1, 3, 2]) - Add [1, 3, 2] to result
|  |  |  |  |  |  |
|  |  |  |  |  |  |--backtrack([1, 3]) - Pop 2, mark 2 as unvisited
|  |  |  |  |  |
|  |  |  |  |  |--choose 2 (already visited, skip)
|  |  |  |  |
|  |  |  |  |--backtrack([1]) - Pop 3, mark 3 as unvisited
|  |  |
|  |  |--choose 2
|  |  |  |
|  |  |  |--backtrack([2])
|  |  |  |  |
|  |  |  |  |--choose 1
|  |  |  |  |  |
|  |  |  |  |  |--backtrack([2, 1])
|  |  |  |  |  |  |
|  |  |  |  |  |  |--choose 3
|  |  |  |  |

```