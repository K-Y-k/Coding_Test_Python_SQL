# M 만큼 반복하여 i~j까지의 인덱스에 k 값을 넣는다.

import sys

N, M = map(int, input().split())

num_li = [0] * N

for _ in range(M):                                    # M 만큼 반복하여
    i, j, k = map(int, sys.stdin.readline().split()) 
    
    for g in range(i-1, j):                           # i~j까지의 인덱스
        num_li[g] = k                                 # k 값을 넣는다.

answer = ' '.join(map(str, num_li))
print(answer)