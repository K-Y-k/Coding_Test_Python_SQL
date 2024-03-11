# 재귀를 활용한 방식

def factorial(n):
    if n <= 1:                                   # 1보다 작거나 같으면 1이므로 1로 반환하고
        return 1
    else:                                        # 1보다 크면 현재 값 x n-1일 때의 재귀호출을 한다.
        return n * factorial(n-1)

N = int(input())
print(factorial(N))



# 반복문 활용 방식

N = int(input())

answer = 1

for i in range(1, N+1):
    answer *= i

print(answer)

