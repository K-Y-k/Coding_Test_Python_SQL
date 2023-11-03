# 넓이 계산 후 출력

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    answer = N * N
    
    print('#' + str(test_case), answer)