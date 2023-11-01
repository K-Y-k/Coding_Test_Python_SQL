# 3명씩 나누는 조의 최대 값이므로

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    answer = N // 3
    
    print('#' + str(test_case), answer)