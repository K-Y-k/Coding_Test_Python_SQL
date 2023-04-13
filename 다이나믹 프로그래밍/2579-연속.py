# 계단 마지막은 무조건 밟아야하므로
# 점화식
# 1. 마지막을 밟고 이전 계단을 연속해서 밟은 경우 ->      밟음(dp[i-3])             X            밟음(stair[i-1])   밟음(stair[i])
# 2. 마지막을 밝고 전전 계단을 밟은 경우         ->                            밟음(dp[i-2])        X              밟음(stair[i])
# 이 2가지의 경우의 수 중 최대 값을 구한다.


import sys

N = int(input())                                              # 계단 개수 입력
stair = [0] * 301                                             # 계단 값 초기화
d = [0] * 301                                                 # dp 값 초기화
 
for i in range(N): 
    stair[i] = int(sys.stdin.readline())                      # 계단 개수에 맞게 계단 값 넣기
    
d[0] = stair[0]                                               # 계단수가 3개까지는 최대값이 오는 경우의 수가 다르기에 각 케이스에 맞게 일일히 초기화
d[1] = stair[0] + stair[1]
d[2] = max(stair[1]+stair[2], stair[0]+stair[2]) 

for i in range(3, N):                                         # 계단 개수가 3개 이상이면
    d[i] = max(d[i-3]+stair[i-1]+stair[i], d[i-2]+stair[i])   # 위 점화식 2가지를 넣고 최대값을 넣는다.

print(d[N-1])                                                 # dp 마지막 항의 값이 최대값