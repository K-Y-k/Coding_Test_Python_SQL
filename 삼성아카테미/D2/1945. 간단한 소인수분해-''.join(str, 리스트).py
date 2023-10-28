# 문제에서 제한한 소수의 값들을 리스트를 저장하고
# 문제에서 주어진 값을 0이 될 때까지 각 소수 값을 나누며 각 소수가 몇번 나눴는지 저장해가며 진행한다.

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