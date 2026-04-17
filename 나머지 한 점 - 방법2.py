def solution(v):
    x_list = [p[0] for p in v]
    y_list = [p[1] for p in v]
    
    # 한 번만 등장하는 값 찾기
    x = [i for i in x_list if x_list.count(i) == 1][0]
    y = [i for i in y_list if y_list.count(i) == 1][0]
    
    return [x, y]
