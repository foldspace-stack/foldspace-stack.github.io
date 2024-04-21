from typing import *


def solution(matrix: List[List[int]]):
    length = len(matrix)
    for i in range(length // 2): # 循环上半部分
        for j in range(i, length - i - 1): #循环
            temp = matrix[i][j]
            matrix[i][j] = matrix[length - 1 - j][i] # 左下移动到左上
            matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j] # 右下移动到左上
            matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
            matrix[j][length - 1 - i] = temp
