from typing import List

"""
最长的不重复字符串
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj
暴力破解

"""


def solution(s: str):
    tmp_chars:set=set([])
    max_length=0
    for i_index,char_i in enumerate(s):
        _length = 0
        for charj in s[i_index:]:
            if charj in tmp_chars:
                break
            _length+=1
            tmp_chars.add(charj)
        max_length = max(max_length,_length)
        tmp_chars=set([])
    return max_length
            
        


if __name__ == '__main__':
    s = "abcabcbb"
    print(solution(s))
