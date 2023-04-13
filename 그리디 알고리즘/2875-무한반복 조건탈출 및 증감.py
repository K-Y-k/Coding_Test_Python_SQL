N, M, K = map(int, input().split())

result = 0

while True:
    N -= 2                          # 여학생 짝을 짓는 수 감소
    M -= 1                          # 남학생 짝을 짓는 수 감소
    
    if N<0 or M<0 or (N+M)<K:       # 짝을 짓는 수가 충족하지 못했을 경우 + 인턴으로 보내야하는 수보다 작으면 
        break                       # 반복문을 종료
        
    result += 1                     # 위 조건을 충족했을 경우 팀 수 증가 
    
print(result)                       # 최종 팀 수 출력
