# 최대공약수와 최소공배수 활용 방식
# ZeoDivisionError 발생

import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b, c, d, e, f = map(int, input().split())

# x_lcm = math.lcm(a, d)
x_lcm = a * d // gcd(a, d)

y_a = (x_lcm // a) * b - (x_lcm // d) * e
y_result = (x_lcm // a) * c - (x_lcm // d) * f


y = y_result // y_a
x = (c - b*y) // a

print(x, y)


# 근의 공식 활용 방식

a, b, c, d, e, f = map(int, input().split())

x = (c*e - f*b) // (a*e - d*b)
y = (c*d - f*a) // (b*d - e*a)

print(x, y)


# 브루트포스 방식
# 연산횟수가 적으면 일일히 루프를 돌아 대입해가며 확인할 수 있다.

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            break