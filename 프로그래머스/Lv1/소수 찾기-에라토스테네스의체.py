# 에라토스테네스의 체만 구현하면 쉽게 풀린다.


def solution(n):
    answer = 0
    
    prime = [True] * 1000001            # 문제에서 1000000까지라고 했으므로
    prime[0], prime[1] = False, False   # 0과 1은 소수가 아니므로 따로 지정
    is_prime(prime)
    
    for i in range(2, n+1):
        if prime[i]:
            answer += 1
    
    return answer

# 에라토스테네스의 체
def is_prime(prime):
    for i in range(2, 1000001):
        if prime[i] == True:
            j = i*i
            
            while j < 1000001:
                prime[j] = False
                j += i