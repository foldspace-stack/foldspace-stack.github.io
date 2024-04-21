# 题目

https://leetcode.cn/problems/search-in-rotated-sorted-array/?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj

![](attachments/Pasted%20image%2020240301211350.png)

# 解题

要求算法复杂度 所以应该确定解
肯定不能循环 循环就 `O(n)` 了
题目基本上  就是查找 元素  二分搜索 `O(log n)`


# 二分搜索

```python
def solution(nums: list, target: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2 # 每次区间的中间值
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:  # target 在左边
            if nums[left] <= target <= nums[mid]:
                # 左边区间有序
                right = mid - 1
            else:
                left = mid + 1
        else:  # target 在右边
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

```


