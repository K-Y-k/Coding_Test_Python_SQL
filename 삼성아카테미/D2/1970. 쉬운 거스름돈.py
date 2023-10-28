# 문제에서 거스를 수 있는 돈을 큰 순으로 저장하고
# 큰 거스름 돈부터 최대한 거스르게 한다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    coin_li = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = []
    
    for i in coin_li:
        count = N // i
        
        answer.append(count)
        N -= count * i
    
    print('#' + str(test_case))
    print(' '.join(map(str, answer)))