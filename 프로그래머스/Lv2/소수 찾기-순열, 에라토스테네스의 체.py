# 내가 푼 방식
# 에라토스테네스의 체 로직을 구현하여 문제에서 주어진 최대 숫자까지 미리 소수를 판별해 놓았고
# 순열로 각 조합하여 해당 숫자가 소수인지 + 이미 전에 나왔던 숫자인지 검사하여 소수이면 카운팅하였다.


from itertools import permutations

def is_prime(prime):                 # 에라토스테네스의 체 로직을 구현하여 문제에서 주어진 최대 숫자까지 미리 소수를 판별해 놓았고
    for i in range(2, 9999999):
        if prime[i] == True:
            j = i * i
        
        while j < 9999999:
            prime[j] = False
            j += i

def solution(numbers):
    answer = 0
    num_list = []                                            # 문자형인 numbers를 각 자리 숫자로 저장하기위한 리스트
    set_dic = []                                             # 중복인지 확인하기 위해 넣을 리스트
    
    
    prime = [True] * 9999999                                 
    prime[0] = False                                         # 0과 1은 소수가 아니므로 미리 초기화
    prime[1] = False
    
    is_prime(prime)                                          # 9999999까지 에라토스테네스체를 적용완료
    
    
    for i in numbers:
        num_list.append(int(i))
    
    
    for i in range(1, len(numbers)+1):                       # 순열로 각 가짓수를 조합하여
        p = permutations(num_list, i)
        
        for j in p:
            temp = ''
            for k in j:
                temp += str(k)
            
            if prime[int(temp)] and int(temp) not in set_dic: # 해당 숫자가 소수인지 + 이미 전에 나왔던 숫자인지 검사하여 소수이면 카운팅하였다.
                set_dic.append(int(temp))
                answer += 1
        
    
    return answer