# 내가 시도해본 방식
import sys

while True:
    N = int(sys.stdin.readline())
    
    prime_list = []
    
    for i in range(3, N, 2):
        count = 0
        
        for j in range(1, i+1):
            if i % j == 0 :
                count += 1
                
            if j == i:
                if count == 2:
                    prime_list.append(i)
    for i in prime_list:
        if N-i in prime_list:
            print(f'{N} = {i} + {N-i}')
            break



# 에라토스체를 활용한 골드바흐 추측
import sys

# 에라토스테네스의 체 : 2부터 +1씩 해주면서 그 배수에 해당하는 값들을 False로 바꿔 소수(=True)를 구분한다.
eratosthenes = [True for i in range(1000001)]   # 전체 수 만큼 True값으로 리스트를 생성

for i in range(2, 1001):                                # n의 최대 약수는 sqrt(n)이하이므로sqrt(1000001) = 1001까지 검사한다. 
    if eratosthenes[i]:                                 # 2부터 +1씩 해주면서 그 배수에 해당하는 값들을 False로 바꿔 소수(=True)를 구분한다.
        for j in range(i+i, 1000001, i):
            eratosthenes[j] = False

while True:
    N = int(sys.stdin.readline())

    if N == 0: 
        break

    check = False                                       # 없을 시의 제약을 걸고 있지만 골드바흐 추측은 무조건 존재할 것이므로 없어도 되긴함
    
    for i in range(3, N, 2):                            # 골드바흐 추측은 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낸다이므로 홀수 3부터 2간격을 주어 홀수들만 조회
        if eratosthenes[i] and eratosthenes[N-i]:       # 현재 i와 N-i가 소수(=True)이면 그 홀수들의 합이 된다는 뜻이므로 출력 
            print(f'{N} = {i} + {N-i}')
            check = True
            break
            
    if check == False:
        print("Goldbach's conjecture is wrong.")
 
            