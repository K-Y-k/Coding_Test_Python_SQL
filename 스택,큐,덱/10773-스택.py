# 0을 입력시 가장 최근 값을 지워야하므로 이때 스택이 떠올라야한다!


import sys

K = int(input())                            # 횟수 입력
stack = []

for _ in range(K):                          # 입력한 횟수만큼 반복
    num = int(sys.stdin.readline())         # 넣을 숫자 입력
    
    if num == 0:                            # 넣은 숫자가 0이면 
        stack.pop()                         # 가장 최근 숫자를 지운다.
    else:                                   # 그 외 숫자는 
        stack.append(num)                   # 넣는다.

print(sum(stack))                           # 넣어진 모든 숫자의 합 출력