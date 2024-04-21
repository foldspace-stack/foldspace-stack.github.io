# 题目

https://leetcode.cn/problems/maximum-subarray/?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj

![[Pasted image 20240305123846.png]]

# 解题

也是中等 

连续 应该不用回溯重排
暴力应该循环一次 
提示`O(n)` 应该纸需要循环一次， 所以需要技巧

规则就是
1. 每次循环
	1. 当前元素> 之前元素的和 直接从这个元素往后加
	2. 没有就累加，
2. 

```python
from typing import *


def solution(nums: List[int]):
    sum_max = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        """
        -2
        1 -> -1,-2 -> -1  
        -3 -> 
        4
        -1
        """
        current_sum = max(num, current_sum + num)
        sum_max = max(current_sum, sum_max)
    return sum_max

```

题目提示了分治法 

当使用分治法来解决最大子数组和问题时，我们可以采用以下思路：

1. 将数组分成左右两部分，分别求出左右两部分的最大子数组和。
2. 然后再考虑跨越中点的情况，找出包含中点的最大子数组和。
3. 最终比较三种情况的结果，取其中的最大值作为最终的结果。

下面是用 Python 实现的分治法解决最大子数组和问题的代码：

```python
def maxSubArray(nums):
    # 辅助函数，用于求解跨越中点的最大子数组和
    def maxCrossingSum(nums, left, right, mid):
        # 从中点向左扫描，找出包含中点的最大左子数组和
        max_left_sum = float('-inf')
        left_sum = 0
        for i in range(mid, left - 1, -1):
            left_sum += nums[i]
            max_left_sum = max(max_left_sum, left_sum)
        
        # 从中点向右扫描，找出包含中点的最大右子数组和
        max_right_sum = float('-inf')
        right_sum = 0
        for i in range(mid + 1, right + 1):
            right_sum += nums[i]
            max_right_sum = max(max_right_sum, right_sum)
        
        # 返回包含中点的最大子数组和
        return max_left_sum + max_right_sum
    
    # 主函数，用于求解最大子数组和
    def divideAndConquer(nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        # 分别求解左右两部分的最大子数组和
        left_sum = divideAndConquer(nums, left, mid)
        right_sum = divideAndConquer(nums, mid + 1, right)
        # 求解跨越中点的最大子数组和
        cross_sum = maxCrossingSum(nums, left, right, mid)
        # 返回三种情况中的最大值
        return max(left_sum, right_sum, cross_sum)
    
    # 调用主函数
    return divideAndConquer(nums, 0, len(nums) - 1)

# 测试
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))  # 输出应为 6
```

这段代码首先定义了一个辅助函数 `maxCrossingSum` 用于求解跨越中点的最大子数组和，然后定义了主函数 `divideAndConquer` 用于实现分治法的递归求解。最后调用主函数来求解最大子数组和，并进行测试。

希望这段代码能够帮助你理解如何用分治法来求解最大子数组和问题。

分治法解决最大子数组和问题的时间复杂度为 O(n log n)，其中 n 为输入数组的长度。

在分治法中，每次都将数组一分为二，然后递归地求解左右两部分的最大子数组和，这部分的时间复杂度为 O(log n)。而在求解跨越中点的最大子数组和时，需要线性地扫描左右两部分，时间复杂度为 O(n)。因此，总体的时间复杂度为 O(n log n)。

这种时间复杂度比暴力求解的 O(n^2) 要好很多，但比动态规划的 O(n) 稍差一些。然而，分治法的思想和实现方式在其他一些问题上可能会更加高效和直观。