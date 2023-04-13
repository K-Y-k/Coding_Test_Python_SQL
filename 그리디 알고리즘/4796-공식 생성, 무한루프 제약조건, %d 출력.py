import sys

result = 0
i = 1

while True:
    L, P, V = map(int, sys.stdin.readline().split())
    
    if L == 0 and P == 0 and V ==0:                  # 무한 루프를 빠져나가기 위한 제약 조건
        break

    X = V // P                                       #  //은 int형태, /은 float형태로 반환
    Y = V % P

    if Y > L:                                        # 남은 일수(Y)가 캠핑장을 이용할 수 있는 일수(L)보다 많이 남았다면 
        Y = L                                        # 캠핑장을 이용할 수 있는 일수만 이용하게한다.

    result = (L * X) + Y                             # 공식 적용한 결과 연산 

    print("Case %d: %d" %(i, result))

    i += 1