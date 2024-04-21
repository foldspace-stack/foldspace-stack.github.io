from typing import *


def solution(nums: List[int]):
    rst = []

    def backtrack(start, path):
        rst.append(path)
        for i in range(start, len(nums)):
            """
            0，1 ，2 ，3
            0
            [[]]
            start=1
            [[],[1]]
            2->
            
             [[],[1]]
             [[],[2],[1],[1,2]]
[[],[2],[1],[1,2],[3],[2,3],[1,3],[1,2,3]]


            1 [1,]
            2 [2,]
            3 [3,]
            
            
            start=2
            
            """
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return rst


def subsets(nums):
    res = [[]]
    for num in nums:
        res += [curr + [num] for curr in res]
    return res

if __name__ == '__main__':
    print(solution([1]))
    print(solution([1,2]))