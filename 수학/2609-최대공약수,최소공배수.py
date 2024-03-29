def gcd(a, b):                    # 최대공약수 함수
    if b == 0:                    # b가 0이 되면 최대공약수이므로 반환
        return a
    else:
        return gcd(b, a%b)        # b가 0이 될 때까지 재귀호출

A, B = map(int, input().split())  # A, B 선언
G = gcd(A, B)                     # A, B에 gcd 함수 적용
L = A*B//G                        # 최소공배수 구하는 공식

print(G)                          # 최대공약수 출력
print(L)                          # 최소공배수 출력