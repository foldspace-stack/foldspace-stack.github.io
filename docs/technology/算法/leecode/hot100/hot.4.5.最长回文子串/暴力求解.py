def solution(s: str):
    """
    1.双重循环
    """
    result = ''
    total_length = len(s)

    def vaild_is(current_index: int, s: str, check_dp: bool):
        left_index = current_index - 1
        right_index = current_index + 1
        tmp_rst = s[current_index]
        if check_dp:
            if (right_index < total_length and tmp_rst == s[right_index]):
                """
                1. a bb a
                """
                tmp_rst = tmp_rst + s[right_index]
                if right_index >= total_length:
                    return tmp_rst
                # 一种加 一种不加
                right_index += 1
        if left_index < 0 or right_index >= total_length:
            """
            1. 第一位开始时候  left 到了 -1
            """
            return tmp_rst

        while right_index < total_length and left_index >= 0:
            if s[left_index] == s[right_index]:
                tmp_rst = s[left_index] + tmp_rst + s[right_index]
            else:
                break
            left_index -= 1  # 扩散+1
            right_index += 1  # 扩散+1
        print('tmp_rst', tmp_rst)
        return tmp_rst

    for index in range(0, total_length):
        tmp_cs_1 = vaild_is(index, s, False)
        tmp_cs_2 = vaild_is(index, s, True)
        print(index, "tmp_cs_2", tmp_cs_2, "tmp_cs_1", tmp_cs_1)
        tmp_cs = len(tmp_cs_2) > len(tmp_cs_1) and tmp_cs_2 or tmp_cs_1
        if len(tmp_cs) > len(result):
            result = tmp_cs
    return result


if __name__ == '__main__':
    c = solution("aacabdkacaa")
    print(c)
