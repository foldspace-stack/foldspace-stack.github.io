# 题目

![](attachments/Pasted%20image%2020240229175914.png)

# 解题 

分析
1. 构造合适的对象存储数据
2. 对问题 进行归类 适合那种方式解
3. 返回所有组合问题 也可以认为是路径相关， 算是全排列问题 应该可以回溯

回溯的模板如下

```python
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```


```python
def solution(digits: list):
    KEY = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}
    rsts = []

    def backtrace(path, chooise_list):
        if len(chooise_list)==0:
            rsts.append(path)
        else:
            for path_chooice in KEY[chooise_list[0]]:
                backtrace(path+path_chooice,chooise_list[1:])

    if digits:
        backtrace("", digits)
    return rsts

```