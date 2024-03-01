# gcd 알고리즘 구현 방식
# 최소공배수는 두 수를 곱한 후 최대공약수로 나눈 값이다.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


A, B = map(int, input().split())

g = gcd(A, B)
lcm = A * B // g                     # 최소공배수는 두 수를 곱한 후 최대공약수로 나눈 값이다.

print(lcm)



# math 라이브러리의 lcm 함수 사용 방식

import math

A, B = map(int, input().split())

lcm = math.lcm(A, B)

print(lcm)