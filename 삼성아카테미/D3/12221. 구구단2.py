# 주어진 숫자 2개를 받고
# 각 숫자가 10이상이면 -1을 출력하고
# 1~9이면 두 숫자를 곱셈하여 출력

T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    
    if A >= 10 or B >= 10:
        answer = -1
    else:
        answer = A * B
        
    print('#' + str(test_case), answer)