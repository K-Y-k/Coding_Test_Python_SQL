# 야매 풀이
N = int(input())

cnt = 0

for i in range(1, N+1) :  # 팩토리얼은 1부터 N까지 곱하기에 그 만큼 반복 설정
    # N<=500 이므로 5가 추가로 들어가는 것은 125(5x5x5)까지이다.
    if i % 5 == 0 :       # 5로 나누었을 때의 개수를 카운트
        cnt += 1
    
    if i % 25 == 0 :      # 5x5 즉, 5가 2개일 때를 위한 카운트 조건
        cnt += 1
    
    if i % 125 == 0 :     # 5x5x5 즉, 5가 3개일 때를 위한 카운트 조건
        cnt += 1
        
print(cnt)



# 정석 풀이
N = int(input())

def zero_cnt(N): 
    cnt = 0

    while N != 0 :      # 0이 아닐 때까지 
        N //= 5         # 5를 나눈 개수를 순차적으로 카운트한다.
        cnt += N
    return cnt          # 위 반복을 거친 카운트 반환
        
print(zero_cnt(N))      # 카운트 출력