def solution(candidates: list, target: int):
    result = []

    def backtrack(start, path, target):
        if target == 0:
            # 当目标和为0时，将当前路径添加到结果中
            result.append(path[:])
            return
        elif target < 0:
            # 当目标和小于0时，结束当前路径的探索
            return

        for i in range(start, len(candidates)):
            # 选择当前值
            path.append(candidates[i])
            # 递归调用，因为可以重复使用相同的数字，下一轮的起始索引仍为i
            backtrack(i, path, target - candidates[i])
            # 撤销选择
            path.pop()

    backtrack(0, [], target)
    return result

if __name__ == '__main__':
    print('1', solution([2, 3, 6, 7], 7))
    print('2', solution([2, 3, 5], 8))
