# 문제에서의 행렬 곱셈은 N*M 행렬과 M*K 행렬이 만나 N*K행렬을 만든다.

import sys

N, M = map(int, input().split())                                      # N, M 입력
A = []                                                                # A 선언 및 원소 값 넣기
for _ in range(N):                                                    
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))

M, K = map(int, input().split())                                      # M, K 입력
B = []                                                                # B 선언 및 원소 값 넣기
for _ in range(M):
    B.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = [[0]*K for _ in range(N)]                                    # 곱셈한 결과 값 N x K의 행렬로 초기화
for n in range(N):                                                    # N
    for k in range(K):                                                # K
        for m in range(M):                                            # 겹치는 M이 마지막
            # ex) result[1][1] = A[1][1]*B[1][1] + A[1][2]*B[2][1]
            result[n][k] += A[n][m] * B[m][k]                         # 해당 위치의 값을 연산한 값으로 적용
        
for i in result:                                                      # 최종 결과를 각 행마다 출력하게 한 형태
    print(" ".join(map(str, i)))
