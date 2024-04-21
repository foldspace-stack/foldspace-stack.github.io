# 题目

https://leetcode.cn/problems/word-search/?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj

![](attachments/Pasted%20image%2020240306222446.png)

# 解题


这个题目 还是回溯法 


```python
from typing import *


def solution(board: List[List[str]], word: str):
    if not board:
        return False
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    def dfs(board, i, j, word, k, visited):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k] or visited[i][j]:
            return False
        visited[i][j] = True
        res = dfs(board, i + 1, j, word, k + 1, visited) or \
              dfs(board, i - 1, j, word, k + 1, visited) or \
              dfs(board, i, j + 1, word, k + 1, visited) or \
              dfs(board, i, j - 1, word, k + 1, visited)
        visited[i][j] = False
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word, 0, visited):
                return True
    return False

```
