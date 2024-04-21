
def solution(height:list):
    max_area=0
    left_p=0
    right_p=len(height)-1
    while left_p<right_p:
        area = min(height[left_p],height[right_p])*(right_p-left_p)
        if area > max_area:
            max_area=area
        if height[left_p] < height[right_p]:
            left_p+=1
        else:
            right_p-=1
    return max_area