import sys

def gcd(a, b):                                      # 최대공약수 함수
    if b == 0:                                      # b가 0이 되면 최대공약수이므로 반환
        return a
    else:
        return gcd(b, a%b)                          # b가 0이 될 때까지 재귀호출


N = int(input())                                    # 입력 횟수 선언

for _ in range(N) :                                 # 입력 횟수만큼 반복
    A, B = map(int, sys.stdin.readline().split())   # A, B 입력 값 선언

    G = gcd(A,B)                                    # 최대공약수 구하는 함수 적용
    result = A*B//G                                 # 최소공배수 공식 적용 계산

    print(result)                                   # 결과출력