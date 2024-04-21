def solution(s: str):
    """
    栈道记录一个 最早连续的下标 和 ( 的下标
    如果 未匹配 移动 最早下标
    """
    stack = [-1]
    max_length = 0
    for index in range(len(s)):
        """
        )((() 
        """
        if s[index] == '(':
            # 存入当前下标
            # 表示有未匹配的（
            stack.append(index) # 存入当前起点位置
        else:
            # 栈道本类有一个元素
            # 消掉为之后为最早的下标
            stack.pop()
            if not stack:
                # 没有被匹配 移动最早的下标
                stack.append(index)  
            else:
                # 匹配了 计算 上一个 （ 的差值
                cur_length = index - stack[-1] # 
                max_length = max(cur_length, max_length)
    return max_length


if __name__ == '__main__':
    s=solution("()()()()(())")
    print(s)