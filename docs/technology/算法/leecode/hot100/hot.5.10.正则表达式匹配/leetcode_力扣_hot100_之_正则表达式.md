# 题目

给你一个字符串 `s` 和一个字符规律 `p`，请你来实现一个支持 `'.'` 和 `'*'` 的正则表达式匹配。

- `'.'` 匹配任意单个字符
- `'*'` 匹配零个或多个前面的那一个元素

所谓匹配，是要涵盖 **整个** 字符串 `s`的，而不是部分字符串。

 

**示例 1：**
```
**输入：**s = "aa", p = "a"
**输出：**false
**解释：**"a" 无法匹配 "aa" 整个字符串。
```

**示例 2:**

```

**输入：**s = "aa", p = "a*"
**输出：**true
**解释：**因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
```


**示例 3：**

```
**输入：**s = "ab", p = ".*"
**输出：**true
**解释：**".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

```

**提示：**

- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- `s` 只包含从 `a-z` 的小写字母。
- `p` 只包含从 `a-z` 的小写字母，以及字符 `.` 和 `*`。
- 保证每次出现字符 `*` 时，前面都匹配到有效的字符

# 解法


## 动态规划


### 问题拆解，确定状态

1. 使用`dp[i][j]`来表示`s[i]`是否与`p[j]`能够匹配，能则为`true`，否则为`false`

### 确定状态转移方程

pattern 为正则字符串

dp 的初始状态 `dp[0][0]=True` 

1. 字母： `dp[i][j]=dp[i-1]dp[j-1] and pattern[j]==s[i]`
2. `.`  :  `dp[i][j]=dp[i-1]dp[j-1]`
3.  `*` : 转换 `dp[i][j]=dp[i-1]dp[j-1] and pattern[j]=='*'`
	1. pattern前面一位为字母   根据前一段的匹配值 `s[i-1] == p[j-1]`
	2. pattern前面一位为 `*`  `dp[i-1][j]`  或者 `dp[i][j-2]`
	3. pattern 前面一位为 `.`  `True`

### 确定扫描路径,递推方程推导

1.  i `0-len`
2. j `0-len``

### 构造结果

1. 用一个全局变量存结果



# 参考

1. https://biaodigit.github.io/LeetCode/0010/#%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF-%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92
2. https://developer.aliyun.com/article/1056825