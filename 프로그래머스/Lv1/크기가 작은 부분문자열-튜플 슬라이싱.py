# 내가 푼 방식
# 각 인덱스에서 p의 길이만큼으로 이어 붙인 값이 p보다 작거나 같으면 카운팅해주었다.


def solution(t, p):
    answer = 0
    
    for i in range(len(t)-len(p)+1):       
        if int(t[i:i+len(p)]) <= int(p):   # 각 인덱스에서 p의 길이만큼으로 이어 붙인 값이 p보다 작거나 같으면
            answer += 1                    # 카운팅해주었다.
    
    
    return answer