S = int(input())             # 입력 값 선언 
n = 1                        # 1부터 더한 값을 하나씩 증가해서 확인하므로 n의 첫 값 1선언 

while n * (n+1) / 2 <= S :   # 더한 자연수의 개수가 최대 값이 되려면 1부터 n까지의 등차수열의 합인  n * (n+1) / 2에 제일 근접한 값의 자연수 개수가 최대 값이 된다.
    n += 1                   # n을 하나씩 증가 시키면서 최대 개수 값 확인

print(n-1)                   # 같거나 작을 때까지 반복하여  최근 n에 +1이 된  상태이므로  -1을 해서 결과 출력