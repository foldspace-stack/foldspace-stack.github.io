#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2023/7/15 01:17
# @author  : timger/yishenggudou
from typing import List


def solution(nums: List[int], target: int):
    memo = {}
    for i, elem in enumerate(nums):
        x = target - elem
        print(memo)
        if memo.get(elem) is not None:
            return [memo[elem], i]
        memo[x] = i


if __name__ == '__main__':
    _ = solution([2, 7, 11, 15], 9)
    print(_)
    assert _ == [0, 1]
