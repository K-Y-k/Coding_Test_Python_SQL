# 내가 시도한 방식 : 일부 테스트 케이스만 맞음
# 알파벳이 나열된 리스트를 미리 선언하고
# 각 단어를 조회할 때 해당 단어의 인덱스를 찾고 
# 문제에서 주어진 인덱스 만큼 띄어넘는데 이때 skip에 해당하는 단어인 경우는 따로 처리

def solution(s, skip, index):
    answer = ''

    # 알파벳이 나열된 리스트를 미리 선언하고
    alpha_list = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    
    for i in s:
        idx = alpha_list.index(i)            # 각 단어를 조회할 때 해당 단어의 인덱스를 찾고 
        count = 0                            # 문제에서 띄어넘으라는 개수 만큼 카운팅할 값 초기화
         
        while count < index:                 # 문제에서 주어진 인덱스 만큼 띄어넘는데
            if idx == len(alpha_list)-1:     # 끝의 단어까지 왔는데 count가 덜 찼으면
                idx = 0                      # 제일 앞의 인덱스로 조정해주고
                count += 1                   # 카운팅
                continue
            
            if alpha_list[idx] not in skip:  # skip에 해당되지 않는 단어인 경우
                idx += 1
                count += 1
            else:                            # skip에 해당하는 단어인 경우
                idx += 1
                
        answer += alpha_list[idx]
                
            
    return answer


# 끝 단어가 앞으로 오는 방식인데
# 문제에서 띄어넘는 개수의 최대가 20개, skip의 최대가 10개이므로 최대 30번을 띄어넘을 수 있어 
# 처음 리스트 선언할 때 a~z를 3번 이어붙이면 인덱스에 대한 처리를 따로 하지 않아도 된다.
# skip에 해당하는 단어는 미리 제거해주면 띄어넘을 때 따로 인덱스를 조절할 필요가 없어져 편리하게 진행할 수 있다. 

def solution(s, skip, index):
    answer = ''

    # 문제에서 띄어넘는 개수의 최대가 20개, skip의 최대가 10개이므로 최대 30번을 띄어넘을 수 있어 
    # 처음 리스트 선언할 때 a~z를 3번 이어붙이면 인덱스에 대한 처리를 따로 하지 않아도 된다.
    alpha_list = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']*3
    
    
    for i in skip:              # skip에 해당하는 단어는 미리 제거해주면 띄어넘을 때 따로 인덱스를 조절할 필요가 없어져 편리하게 진행할 수 있다. 
        alpha_list.remove(i)
        alpha_list.remove(i)
        alpha_list.remove(i)
        
    for i in s:
        idx = alpha_list.index(i)
        answer += alpha_list[idx+index]
                
    
    return answer