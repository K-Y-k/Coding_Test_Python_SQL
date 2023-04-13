# 내가 푼 방식
# 초반 부분에만 패턴이 다르다가
# P(N) 값이 9부터는 [현재위치-5]의 값 + [현재위치-1]의 값이 들어간다.
# 이를 점화식으로 세워서 진행

import sys

T = int(input())

d = [0] * 100

PN = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(len(PN)):
    d[i] = PN[i]

for _ in range(T):
    N = int(sys.stdin.readline())
    
    if N > 9:
        for i in range(10, N):
            d[i] = d[i-5] + d[i-1]
            
        print(d[N-1])
    else:
        print(d[N-1])




# 좀 더 효율적인 정답
# P(4)부터 P(N-3) + P(N-2)의 값이 들어간다.
# ex) P[4] = P[1] + P[2]
#     P[5] = P[2] + P[3]
#     P[6] = P[3] + P[4]
#     P[7] = P[4] + P[5]
#     P[8] = P[5] + P[6]

import sys

d = [0] * 101

d[0] = 1
d[1] = 1
d[2] = 1

for i in range(3, 101):           # 미리 올 수 있는 최대값까지 모두 위 패턴 값들로 적용
    d[i] = d[i-3] + d[i-2]

    
T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(d[N-1])