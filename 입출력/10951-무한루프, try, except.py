import sys

while True :  # 무한 루프
    try :     # 잘못 입력으로서의 예외 처리 
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except :
        break