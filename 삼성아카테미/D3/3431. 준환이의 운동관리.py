# 최소 운동시간보다 작을 때
# 최소~최대 운동시간 사이일 때
# 최대 운동시간보다 클 때
# 3가지 케이스에 따른 문제에서 원하는 답으로 출력

T = int(input())

for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    
    if L <= X <= U:
        answer = 0
    elif X > U:
        answer = -1
    else:
        answer = L - X
        
    print('#' + str(test_case), answer)