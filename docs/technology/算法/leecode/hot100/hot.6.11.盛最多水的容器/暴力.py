
def solution(height_list:list):
    max_area=0
    for i in range(0,len(height_list)):
        for j in range(0,len(height_list)):
            area=min(height_list[i],height_list[j])*(j-i)
            if area > max_area:
                max_area=area
    return max_area