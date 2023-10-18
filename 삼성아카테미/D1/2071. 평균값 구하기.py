import math

T = int(input())

for test_case in range(1, T + 1):
    li = map(int, input().split())
    answer = 0
    
    for i in li:
        answer += i
    
    answer /= 10
    
    print('#' + str(test_case), round(answer))
    