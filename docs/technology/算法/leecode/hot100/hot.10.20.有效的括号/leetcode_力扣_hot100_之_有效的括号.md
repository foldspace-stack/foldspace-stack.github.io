
# 题目

![[Pasted image 20240229213041.png]]

# 解题

这个可以利用栈的特性 很好地判断

```python
def solution(s: str):
    stack = []
    map = {"}": "{", "]": "[", ")": "("}
    for i in s:
        if len(stack) > 0 and stack[-1] == map.get(i):
            """
            ） 时候 如果 内部 为 （ 弹出
            """
            stack.pop()
        else:
            stack.append(i)


    return len(stack) == 0

```