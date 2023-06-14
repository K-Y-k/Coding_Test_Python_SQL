# 에라토스테니스의 체로 소수를 미리 판별해 놓은 곳에
# 조합으로 뽑은 3개의 숫자의 합을 위 소수 판별된 배열에 넣어 소수인지에 따라 카운팅


from itertools import combinations

def solution(nums):
    answer = 0
    
    prime = [True] * 2972                          # 1000까지이므로 3개를 뽑을 때의 최대값이 1000 999 998이라 (근데 2972까지만 해도 됨;)
    is_prime(prime)
    prime[0], prime[1] = False, False

    combination_nums = list(combinations(nums, 3)) # 조합으로 뽑은 3개의 숫자의 조합 리스트
    
    for i in combination_nums: 
        total_sum = sum(i)                         # 조합으로 뽑은 3개의 숫자의 합을
        
        if prime[total_sum] == True:               # 위 소수 판별된 배열에 넣어 소수인지에 따라 카운팅
            answer += 1
    

    return answer

# 에라토스테네스의 체
def is_prime(prime):
    for i in range(2, 2972):
        if prime[i] == True:
            j = i*i
            
            while j < 2972:
                prime[j] = False
                j += i