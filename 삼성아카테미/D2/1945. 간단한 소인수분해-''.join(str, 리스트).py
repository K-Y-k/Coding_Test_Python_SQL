T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    prime_li = [2, 3, 5, 7, 11]
    
    answer = [0, 0, 0, 0, 0]
    
     
    for i, value in enumerate(prime_li):
        while N % value == 0:
            answer[i] += 1
            N //= value
    
    a = ' '.join(map(str, answer))
    
    print('#'+ str(test_case), a)