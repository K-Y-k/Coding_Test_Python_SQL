# A와 B시간을 더한 후
# 24시간의 시계 기준으로 다시 구해주기

T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    
    answer = 0
    answer += (A + B)
    answer %= 24
    
    print('#' + str(test_case), answer)