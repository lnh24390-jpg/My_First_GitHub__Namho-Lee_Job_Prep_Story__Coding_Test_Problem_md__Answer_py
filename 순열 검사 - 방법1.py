def solution(arr):
    n = len(arr)
    
    # 중복 제거 + 값 비교
    return set(arr) == set(range(1, n + 1))
