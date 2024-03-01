# 내가 푼 방식 - math 라이브러리의 gcd함수 활용 방식
# 기약분수 구하는 법은 
# 두 분모를 서로 곱한 후 최대 공약수로 나눈 값이 기약분모(=최소공배수)가 되고
# 두 분자는 반대 분모 값으로 곱한 후 서로 더하고 최대 공약수로 나눈 값이 기약분자가 된다.

import math

answer = []

A_child, A_parent = map(int, input().split())
B_child, B_parent = map(int, input().split())

sum_child = (A_child * B_parent) + (B_child * A_parent)      # 두 분모를 서로 곱한 후 
common_parent = (A_parent * B_parent)                        # 두 분자를 반대 분모 값으로 곱한 후 서로 더하고

g = math.gcd(sum_child, common_parent)                       # 최대공약수

answer.append(sum_child // g)                                # 최대 공약수로 나눈 값이 기약분자가 된다.
answer.append(common_parent // g)                            # 최대 공약수로 나눈 값이 기약분모(=최소공배수)가 된다.

print(' '.join(map(str, answer)))



# 직접 최대공약수(gcd) 알고리즘 구현한 방식

def gcd(a, b):                                               # gcd 알고리즘
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

answer = []

A_child, A_parent = map(int, input().split())
B_child, B_parent = map(int, input().split())

sum_child = (A_child * B_parent) + (B_child * A_parent)
common_parent = (A_parent * B_parent)

g = gcd(sum_child, common_parent)

answer.append(sum_child // g)
answer.append(common_parent // g)

print(' '.join(map(str, answer)))

