from typing import *


def solution(matrix: List[List[int]]):
    n = len(matrix)
    # 转置矩阵
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # 反转每一行
    for i in range(n):
        matrix[i].reverse()
