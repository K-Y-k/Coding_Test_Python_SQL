T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    
    a = map(int, input().split())
    
    for i in a:
        if i % 2 == 1:
            answer += i
    
    print('#' + str(test_case),  answer)
    