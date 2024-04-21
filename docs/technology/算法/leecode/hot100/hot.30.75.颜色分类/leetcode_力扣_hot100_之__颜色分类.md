# 题目

https://leetcode.cn/problems/sort-colors?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj

![](attachments/Pasted%20image%2020240306152459.png)

# 解题

排序问题， 
不能 sort 那就应该 自己实现


 颜色分类（Sort Colors）是一道关于数组排序的问题，题目要求按照红、白、蓝的顺序对数组进行排序。有几种常见的解题思路和解法，包括三路快排、计数排序和双指针法。下面分别用 Python 展示这几种解法：

### 三路快排

```python
def sortColors(nums):
    left, curr, right = 0, 0, len(nums) - 1
    while curr <= right:
        if nums[curr] == 0:
            nums[left], nums[curr] = nums[curr], nums[left]
            left += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1
        else:
            curr += 1
```

### 计数排序

```python
def sortColors(nums):
    count = [0, 0, 0]
    for num in nums:
        count[num] += 1
    
    idx = 0
    for color, cnt in enumerate(count):
        for _ in range(cnt):
            nums[idx] = color
            idx += 1
```

### 双指针法

```python
def sortColors(nums):
    red, white, blue = 0, 0, len(nums) - 1
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            white += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
```

以上是三种常见的解题思路和对应的 Python 实现。三路快排和双指针法都是在原地排序的方法，而计数排序则需要额外的空间。根据实际情况选择合适的解法即可。