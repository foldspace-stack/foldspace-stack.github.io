from typing import *
def solution( strs: List[str]):
    rst_map={}
    for s in strs:
        key=''.join(sorted(s))
        if key in rst_map:
            rst_map[key].append(s)
        else:
            rst_map[key]=[s,]
    return list(rst_map.values())