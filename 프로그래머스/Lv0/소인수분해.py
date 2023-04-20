def solution(n):
    answer = []
    prime_list = []
    count = 2
    
    while count <= n:
        if n % count == 0:
            prime_list.append(count)
            n //= count
            
        count += 1
        
    for i in prime_list:
        if i not in answer:
            answer.append(i)
    
    return answer