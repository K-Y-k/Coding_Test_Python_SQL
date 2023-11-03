# 일반 거듭제곱 방식

for _ in range(10):
    test_case = int(input())
    N, multi = map(int, input().split())
    
    answer = N ** multi
    
    print('#' + str(test_case), answer)



# 재귀를 사용한 방식

for _ in range(10):
    test_case = int(input())
    N, M = map(int, input().split())
    
    def power(N, M):
        if M == 0:
            return 1
        else:
            return N * power(N, M-1)
    
    
    print('#' + str(test_case), power(N, M))