# 내가 시도한 방식 = 일부 테케만 맞음

T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    
    anwer = 0
    
    if W * P <= Q:
        answer = W * P
    else:
        answer = Q + (W - R) * S
    
    print('#' + str(test_case), answer)



# 정답

T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    
    A = W * P
    B = Q
    
    if W > R:
        B += (W - R) * S
    
    if A > B:
        print('#' + str(test_case), B)
    else:
        print('#' + str(test_case), A)