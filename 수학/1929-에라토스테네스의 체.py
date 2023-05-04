MAX = 1000000                                # (1 ≤ M ≤ N ≤ 1,000,000)이므로 최대 설정
prime = [True for _ in range(MAX+1)]         # 배열 공간 최대 설정
prime[0] = prime[1] = False                  # 0과 1은 소수가 아니므로 False로 미리 대상에서 제외

for i in range(2, MAX+1):                    # 에라토스테네스의 체
    if prime[i] == True:                     # 소수이면
        j = i*i                              # i x i를 해서
        
        while j < (MAX+1):                   # i x i가 최대 값보다 작을 때까지
            prime[j] = False                 # 배수들은 False로 지워줘 결국 True인 것은 소수만 남을 것이다.
            j += i                           # i*(i+1)식으로 증가해야 하므로 i를 더한 것이다.
                
                
M, N = map(int, input().split())             # 입력 값 선언
            
for i in range(M, N+1):
    if prime[i]:                             # True인 것이 소수였으므로 소수 출력
        print(i)