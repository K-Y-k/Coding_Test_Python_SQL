# 1,2,4를 담은 배열을 활용하여
# 현재 숫자 n에 -1을 한 다음 나머지 연산의 나머지가 위 1,2,4 배열의 인덱스가 되고 이 값이 각 자리 수가 되고
# n-1에 3을 나눈 몫이 0이 될 때까지 각 자리수를 넣는 연산을 반복한다. 
# 해당 각 자리 수는 1의 자리부터 저장된 것이므로 마지막에는 반대로 뒤집어야 한다. 


def solution(n):
    answer = ''
    num_list = ['1','2','4']             # 1,2,4를 담은 배열을 활용하여
    
    while n > 0:
        n_persent = (n-1) % 3            # 현재 숫자 n에 -1을 한 다음 나머지 연산의 나머지가 
        
        answer += num_list[n_persent]    # 위 1,2,4 배열의 인덱스가 되고 이 값이 각 자리 수가 되고
        
        n = (n-1) // 3                   # n-1에 3을 나눈 몫이 0이 될 때까지 각 자리수를 넣는 연산을 반복한다. 
        
    
    return answer[::-1]                  # 해당 각 자리 수는 1의 자리부터 저장된 것이므로 마지막에는 반대로 뒤집어야 한다. 