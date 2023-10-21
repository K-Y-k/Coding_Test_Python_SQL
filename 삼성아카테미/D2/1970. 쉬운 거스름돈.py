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