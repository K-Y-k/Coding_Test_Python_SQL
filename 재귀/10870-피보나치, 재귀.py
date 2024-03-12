# 재귀를 활용한 방법
# 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이라고 했으므로 각 케이스를 정의하고
# 그외는 Fn-1 + Fn-2이라고 했으므로 이 식으로 함수를 재호출한다.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

N = int(input())
print(fibonacci(N))
