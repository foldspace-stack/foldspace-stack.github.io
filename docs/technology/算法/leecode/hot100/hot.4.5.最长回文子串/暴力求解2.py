def solution(s: str):
    total_len = len(s)
    if total_len <= 1:
        return s
    rst = s[0]
    tmp_max_len = 1

    def vaild(ts: str, left_index: int, right_index: int):
        """
        往中间计算
        """
        while left_index <= right_index:
            if ts[left_index] != ts[right_index]:
                return False
            left_index += 1
            right_index -= 1
        print('s',left_index,right_index)
        return True

    for i in range(0, total_len):
        for j in range(i + 1, total_len):
            sub_str_length=j-i+1
            if sub_str_length > tmp_max_len and vaild(s, i,j):
                print(sub_str_length)
                tmp_max_len = sub_str_length
                rst = s[i:i+tmp_max_len]
    return rst


if __name__ == '__main__':
    c = solution("aacabdkacaa")
    print(c)
