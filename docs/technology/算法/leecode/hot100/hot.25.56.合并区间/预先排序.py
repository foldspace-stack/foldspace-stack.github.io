from typing import *


def solution(intervals: List[List[int]]):
    new_arr = sorted(intervals, key=lambda x: x[0])
    rst = []
    range_stack = []
    for i in range(len(new_arr)):
        """
        i == 0:
            时候
            
        i:
            
        i == last:
            aa
        """
        if i == 0:
            range_stack.append(new_arr[i][0])
            range_stack.append(new_arr[i][1])
        else:
            if len(range_stack) > 0:
                if range_stack[-1] >= new_arr[i][0]:
                    """
                    合并区间
                    [[1,3],[2,6],[8,10],[15,18]]
                    """
                    if range_stack[-1] < new_arr[i][-1]:
                        range_stack.pop()
                        range_stack.append(new_arr[i][-1])
                else:
                    """
                    区间无法合并
                    """
                    rst.append([range_stack[0], range_stack[-1]])
                    range_stack.pop()
                    range_stack.pop()
                    range_stack.append(new_arr[i][0])
                    range_stack.append(new_arr[i][-1])
            else:
                """
                上一次合并完毕已经加入了区间
                """
                range_stack.append(new_arr[i][0])
                range_stack.append(new_arr[i][-1])
    rst.append([range_stack[0], range_stack[-1]])
    return rst


if __name__ == '__main__':
    print(solution([[1, 3], [2, 6], [8, 10], [15, 18]]
                   ))
