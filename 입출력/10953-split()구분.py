import sys

N = int(input())

for _ in range(N) :
    A, B = map(int, sys.stdin.readline().split(','))  # ,로 구분 입력
    print(A + B)