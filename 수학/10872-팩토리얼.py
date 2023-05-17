# 야매
N = int(input())
sum = 1

for _ in range(N) :
    sum *= N 
    N -= 1
    
print(sum)



# 정석 팩토리얼 함수 로직 활용
def factorial(n):
    if n == 0:                      # n이 0이 될 때까지 반복 호출
        return 1
    else:
        return n * factorial(n-1)   # 재귀 호출

n = int(input())
print(factorial(n))
