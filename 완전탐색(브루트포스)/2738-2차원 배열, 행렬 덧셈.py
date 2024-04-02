# 각 A, B의 행렬을 2차원 배열로 정의해준 후
# 이중 루프로 서로 행과 열에 맞춘 A와 B의 원소들을 더하여 적용했다.

import sys

N, M = map(int, sys.stdin.readline().split())

A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

B = []
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))


answer = [[] for _ in range(N)]

for i in range(N):
    for j in range(M):
        answer[i].append(A[i][j] + B[i][j])


for i in range(N):
    print(' '.join(map(str, answer[i])))



# 따로 저장하지 않고 바로 출력하는 방식
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()