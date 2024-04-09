# 내가 푼 방식 = 시간초과
# 재귀 코드1의 호출되는 횟수는 결국 n이 1이거나 2일 때까지 쪼개진 것이 한번 호출된 것이므로 여기에 카운팅했고
# dp 코드2의 호출되는 횟수는 dp의 각 값을 반복해서 구할 때 호출하므로 카운팅했다.
# 하지만 재귀에서의 시간초과가 발생한 듯하다.

def fibonacci(n):
    global code1Count

    if n == 1 or n == 2:
        code1Count += 1                              # 재귀 코드1의 호출되는 횟수는 결국 n이 1이거나 2일 때까지 쪼개진 것이 한번 호출된 것이므로 여기에 카운팅했고
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


N = int(input())

code1Count = 0
fibonacci(N)
code2Count = 0

dp = [0] * (N+1)
dp[1] = 1
dp[2] = 1


for i in range(3, N+1):
    code2Count += 1                                  # dp 코드2의 호출되는 횟수는 dp의 각 값을 반복해서 구할 때 호출하므로 카운팅했다.
    dp[i] = dp[i-1] + dp[i-2]


print(code1Count, code2Count)



# 극한의 효율 방식
# dp 코드2의 호출되는 횟수는 결국 N-2번 호출한다.
# 재귀 코드1의 호출되는 횟수는 결국 피보나치 함수를 적용한 값과 동일하다.
# 그러므로 재귀 방식의 코드가 아닌 dp 방식의 코드에서의 결과 값으로 적용하면 시간초과가 발생하지 않는다.

N = int(input())

code1Count = 0
code2Count = N-2                                    # dp 코드2의 호출되는 횟수는 결국 N-2번 호출한다.

dp = [0] * (N+1)
dp[1] = 1
dp[2] = 1


for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]


code1Count = dp[N]                                 # 재귀 코드1의 호출되는 횟수는 결국 피보나치 함수를 적용한 값과 동일하다.
                                                   # 그러므로 재귀 방식의 코드가 아닌 dp 방식의 코드에서의 결과 값으로 적용하면 시간초과가 발생하지 않는다.
print(code1Count, code2Count)