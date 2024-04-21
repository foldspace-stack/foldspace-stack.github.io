from typing import List

"""

"""


def solution(s: str, p: str):
    """
    递归
    """
    in_str = s
    pt = p

    if not pt:
        return not in_str

    first_match = bool(in_str) and pt[0] in {in_str[0], '.'}

    if len(pt) >= 2 and pt[1] == '*':
        return (solution(in_str, pt[2:])
                or first_match and solution(in_str[1:], pt))
    else:
        return first_match and solution(in_str[1:], pt[1:])


if __name__ == '__main__':
    print(solution("ab", 'c*ab'))
    assert solution("ab", 'c*ab') is True
