from typing import List

"""
最长的

https://github.com/ascoders/weekly/blob/master/%E7%AE%97%E6%B3%95/199.%E7%B2%BE%E8%AF%BB%E3%80%8A%E7%AE%97%E6%B3%95%20-%20%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E3%80%8B.md


"""


def solution(s: str):
    """
    滑动窗口
    """
    if len(s)<=1:
        return s
    def check_if_is_right(_str, index, j=0):
    
        left = _str[index]
        right = _str[index]
        while left == right:
            if (index - j) < 0 or (index + j + 1) >= len(_str):
                break
            j += 1
            print("j", index, j, index - j, index + j)
            left += _str[index - j]
            right += _str[index + j]
            if left != right:
                j -= 1
        print("jjj:", j,index, left, right)
        if j < 1 and index >= 0 :
            print("fix")
            if _str[index] == _str[index - 1]:
                return 1, "l"
            elif  (index+1) < len(_str) and _str[index] == _str[index + 1]:
                return 1, "r"
        return j, "m"

    def fetch_huiwen_str(current_index, j, flag):
        if flag == 'l':
            _ = s[current_index - 1:current_index + 1]
        elif flag == 'r':
            _ = s[current_index:current_index + 2]
        else:
            _ = s[current_index-j : current_index + j + 1]
        return _

    strs = []
    max_length_tmp = 0
    max_length_str = ""
    for index, c in enumerate(s):
        huiwen_length, flag = check_if_is_right(s, index, 0)
        if huiwen_length > 0:
            _ = (index, huiwen_length + 1, fetch_huiwen_str(index, huiwen_length, flag),flag,huiwen_length)
            strs.append(_)
            if huiwen_length > max_length_tmp or len(_[2]) > len(max_length_str):
                max_length_tmp = huiwen_length
                max_length_str = _[2]
    print(strs,max_length_str)
    return max_length_str


if __name__ == '__main__':
    assert solution("babad") == 'bab'
    assert solution("cbbd") == 'bb'
    assert solution("bb") == 'bb'
    assert solution("aaaa") == "aaaa"
    assert solution("aaaaa") == "aaaaa"
    