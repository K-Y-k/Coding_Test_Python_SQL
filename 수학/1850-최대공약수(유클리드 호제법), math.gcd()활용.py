# math라이브러리에서 gcd함수 제공 방식
import math

A, B = map(int, input().split())

print('1' * math.gcd(A, B))      # 문제에서 메모리가 작게 주어졌기 때문에 수동적으로 표현



# 직접 유클리드 호제법으로 gcd 함수 구현 방식
# 유클리드 호제법은 
#  두 자연수 a, b와 a를 b로 나눈 나머지 r에 대해서
#  a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
#  이를 계속 반복하며 b가 0이 될 때, a값이 바로 최대공약수
import sys

def gcd(a, b) :
    if b == 0 :
        return a
    else :
        return gcd(b, a % b)

A, B = map(int, input().split())

print('1' * gcd(A, B))