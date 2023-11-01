# 평균 값보다 이하일 때 카운팅

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_li = list(map(int, input().split()))
    
    avg_num = sum(num_li) // N
    answer = 0
    
    for i in num_li:
        if i <= avg_num:
            answer += 1
            
    print('#' + str(test_case), answer)