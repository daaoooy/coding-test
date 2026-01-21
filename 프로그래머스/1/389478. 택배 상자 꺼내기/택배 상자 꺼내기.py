import math

def solution(n, w, num):
    total_row = math.ceil(n / w)
    num_row = math.ceil(num / w)
    last_floor_boxes = n - (total_row - 1) * w
    
    if num % w == 0:
        num_col = num % w + w
    else:
        num_col = num % w
    
    if num_row % 2 == 0:
        num_col = w + 1 - num_col
    
    answer = total_row - num_row 

    if (total_row % 2 == 0) and (num_col > (w - last_floor_boxes)):
        answer += 1
    elif (total_row % 2 != 0) and (num_col <= last_floor_boxes):
        answer += 1    

    return answer

solution(22, 6, 8)
solution(13, 3, 6)