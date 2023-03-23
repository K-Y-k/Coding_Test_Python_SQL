import sys
 
N = int(input())

for i in range(1, N+1) :
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {A+B}')                         # print 내부의 값을 동적으로 넣기 위해 print(f' ') 활용