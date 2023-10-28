# A리스트의 크기와 B리스트의 크기를 먼저 비교해서
# 하나의 for문으로 통일 시키기 위해 큰 기준을 고정시키고 시작한다.

T = int(input())

for test_case in range(1, T + 1):
    AN, BN = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    
    if AN > BN:                             # A리스트의 크기와 B리스트의 크기를 먼저 비교해서
        AN, BN = BN, AN                     # 하나의 for문으로 통일 시키기 위해 큰 기준을 고정시키고 시작한다.
        A, B = B, A

    answer = []
    
    for i in range(BN-AN+1) : 
        sum = 0
        
        for j in range(AN) : 
            sum += A[j] * B[i+j]
        
        answer.append(sum)
    
    print('#' + str(test_case), max(answer))