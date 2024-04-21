from typing import *


def solution(heights: List[int]):
    stack = []
    heights.append(0)  # 在高度数组末尾添加一个高度为0的柱形
    max_area = 0
    for i in range(len(heights)):
        """
        [2,1,5,6,2,3]
        
        i:0
        cur:[2]
        stack:[]
        max_area:
        
        i:1
        cur:[1]
        stack:[2]
        """
        print('i', i, stack, heights[i])
        while stack and heights[i] < heights[stack[-1]]:
            """
             1. 当前元素 < 栈道顶部元素(前面一个元素)
             2. 当前元素 > 前面元素 
            """
            h = heights[stack.pop()]
            if not stack:
                """
                栈为空 时候 说明 到了最左边
                宽度 为 i
                """
                w = i
            else:
                """
                栈道不为空的时候  
                """
                w = i - stack[-1] - 1
            print("w", w, 'h', h)
            max_area = max(max_area, h * w)
        # 将元素索引 加入栈
        stack.append(i)
    return max_area


if __name__ == '__main__':
    print('start')
    print(solution([1000000, 0, 1]))
    print('end')
