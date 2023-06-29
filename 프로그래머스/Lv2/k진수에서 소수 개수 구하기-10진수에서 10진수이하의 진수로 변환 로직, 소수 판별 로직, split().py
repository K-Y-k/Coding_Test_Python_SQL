# 내가 푼 방식 : 일부 테스트 케이스 실행 초과 에러
# k진수로 변환한 후 미리 문제에서 주어진 최대 수까지 소수 판별을 해놓은 리스트에 넣어서 확인해보았지만
# 이렇게 전체 크기를 미리 지정하는 과정에서 실행 초과가 발생한 것 같다.

def prime_list(prime):                     # 2부터 최대 값까지 소수 판별 적용 로직
    for i in range(2, 100001):
        if prime[i]:
            j = i*i
            
        while j < 100001:
            prime[j] = False
            j += i

def solution(n, k):
    answer = 0
    
    if k == 10:                            
        k_format = n
    else:                                  # k진수로 변환 로직
        temp = ""

        while n > 0:
            temp += str(n%k)
            n //= k

        k_format = temp[::-1]
    
    prime = [True] * 1000001               # 미리 최대 값까지의 소수 판별 적용을 위한 리스트 선언
    prime[0] = prime[1] = False            # 0과 1은 소수가 아니므로 초깃값 설정
    prime_list(prime)                      # 2부터 최대 값까지 소수 판별 적용
    
    nums = str(k_format).split("0")        # 문제에서 소수에 0이 없어야 하고 주변에 0이 있거나 없으므로 0을 기준으로 쪼갬
    
    for x in nums:                         # 쪼갠 것을 조회하여 '' 공백이 아니거나 소수이면 카운팅
        if x and prime[int(x)]:
            answer += 1
    
    
    return answer



# 소수판별만 하는 로직으로 변경

def format_(n, k):
    temp = ""

    while n > 0:
        temp += str(n%k)
        n //= k

    return temp[::-1]
 
def isPrime(n):                              # 소수판별만 하는 로직
    if n <= 1:
        return False
    
    for i in range(2, int(n**(0.5)+1)):
        if n % i == 0:
            return False
    
    return True

def solution(n, k):
    answer = 0

    k_format = format_(n, k)
    nums = str(k_format).split("0")
    
    for x in nums:
        if x and isPrime(int(x)):
            answer += 1
    
    
    return answer
