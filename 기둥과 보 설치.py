def possible(answer):
    # 현재 구조가 조건을 만족하는지 검사하는 함수
    
    for x, y, a in answer:
        
        # ---------------------------
        # 1. 기둥 검사
        # ---------------------------
        if a == 0:
            # 조건:
            # 바닥 OR 아래 기둥 OR 보의 한쪽 끝
            if y == 0 \
               or [x, y-1, 0] in answer \
               or [x-1, y, 1] in answer \
               or [x, y, 1] in answer:
                continue
            
            return False
        
        # ---------------------------
        # 2. 보 검사
        # ---------------------------
        else:
            # 조건:
            # 한쪽 끝이 기둥 위 OR 양쪽이 보로 연결
            if [x, y-1, 0] in answer \
               or [x+1, y-1, 0] in answer \
               or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            
            return False
    
    return True


def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame:
        
        # ---------------------------
        # 1. 설치
        # ---------------------------
        if b == 1:
            answer.append([x, y, a])
            
            # 설치 후 전체 검사
            if not possible(answer):
                answer.remove([x, y, a])  # 실패 → 롤백
        
        # ---------------------------
        # 2. 삭제
        # ---------------------------
        else:
            answer.remove([x, y, a])
            
            # 삭제 후 전체 검사
            if not possible(answer):
                answer.append([x, y, a])  # 실패 → 롤백
    
    # ---------------------------
    # 3. 정렬
    # ---------------------------
    return sorted(answer)
