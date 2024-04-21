# 题目
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj
![[Pasted image 20240301221934.png]]

# 解题

同上应该也是二分查找但是需要 查找两个 因为元素
两个二分查找 查 `findFirst` 和 `findLast`

```python
def solution(nums: list, target: int):
    def find_first(nums: list, target: int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def find_last(nums: list, target: int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    if len(nums) == 0:
        return [-1, -1]
    first = find_first(nums, target)
    last = find_last(nums, target)
    print(first,last)
    if first <= last:
        return [first, last]
    else:
        return [-1, -1]


if __name__ == '__main__':
    print(solution([5, 7, 7, 8, 8, 10], 8))

```