import sys

while True :
    A, B = map(int, sys.stdin.readline().split())
    if (A != 0 and B != 0) :       # 둘 다 0이 아니면 연산
        print(A + B)
    else :                         # 둘 다 0이면 출력
        break
     
        
    