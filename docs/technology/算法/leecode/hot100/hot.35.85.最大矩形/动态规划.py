from typing import *


def solution(matrix: List[List[str]]):
    if not matrix:
        return 0
    y_length = len(matrix)
    x_length = len(matrix[0])
    left = [0] * x_length  # 初始化左边界
    right = [x_length] * x_length  # 初始化右边界
    height = [0] * x_length  # 初始化高度
    max_area = 0
    for y_i in range(y_length):
        cur_left, cur_right = 0, x_length  # 当前行的左右边界
        # 更新高度
        for x_j in range(x_length):
            if matrix[y_i][x_j] == '1':
                height[x_j] += 1
            else:
                height[x_j] = 0
        # 更新左边界
        for x_j in range(x_length):
            if matrix[y_i][x_j] == '1':
                left[x_j] = max(left[x_j], cur_left)
            else:
                left[x_j] = 0
                cur_left = x_j + 1
        # 更新右边界
        for x_j in range(x_length - 1, -1, -1):
            if matrix[y_i][x_j] == '1':
                right[x_j] = min(right[x_j], cur_right)
            else:
                right[x_j] = x_length
                cur_right = x_j
        # 计算当前行作为底边的最大矩形面积
        for x_j in range(x_length):
            max_area = max(max_area, (right[x_j] - left[x_j]) * height[x_j])
    return max_area
