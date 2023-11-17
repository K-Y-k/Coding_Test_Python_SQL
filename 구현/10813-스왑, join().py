# 입력한 i, j의 위치의 값들을 스왑해준다.


import sys

N, M = map(int, input().split())

num_li = []

for i in range(N):
    num_li.append(i+1)


for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    # 입력한 i, j의 위치의 값들을 스왑해준다.
    temp = num_li[i-1]
    num_li[i-1] = num_li[j-1]
    num_li[j-1] = temp


print(' '.join(map(str, num_li)))