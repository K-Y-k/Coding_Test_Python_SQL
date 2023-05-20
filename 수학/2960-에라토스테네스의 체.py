# 처음에는 모든 값을 True로 만들고 배수를 False에서 적용하는 과정에서 
# 해당 소수와 해당 소수의 배수들을 새로운 리스트에 담는다.

# 예시로 10 7 입력일 때 10까지 차례대로 소수에서 + 소수 배수를 적용한 값을 적용하는 순서이므로
#  2, 4, 6, 8, 10, 3, 9, 5, 7 순서로 담아지기 위해서 새로운 리스트에 담은 것



# 기본 에라토스테네스의 체
def eratoss():
    for i in range(2, N+1):
        if prime[i] == True:                # 현재 값이 True이면
            j = i*i
            
            while j < (N+1):
                prime[j] = False            # 소수의 배수들을 False로 만듬
                j += i

prime = [True] * (N+1)                      # 해당 범위까지의 모든 값을 True로 초기화
eratoss()




# 위 에라토스 테네스의 체를 활용하여 내가 푼 풀이
def eratoss():
    for i in range(2, N+1):
        if prime[i] == True:
            eratoss_list.append(i)          # 소수부분과
            j = i*i
            
            while j < (N+1):
                if prime[j] == True:
                    prime[j] = False
                    eratoss_list.append(j)  # 소수부분의 배수를 차례로 넣는다.
                j += i
    
    
N, K = map(int, input().split())

prime = [True] * (N+1)
eratoss_list = []                           # 문제에서 원하는 형식으로 담기 위한 리스트
eratoss()

print(eratoss_list[K-1])                    # K번째의 값을 출력