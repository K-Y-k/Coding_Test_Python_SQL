# 내가 푼 방식
# 해당 입력해야하는 키가 각 자판기에 인덱스 위치 값을 저장하여 최소 값을 넣어서 최소한의 입력으로 유도했다.
# 각 자판기 모두 해당 키가 없으면 -1이 되므로 이를 처리해주는 것까지 해줘야 한다.



def solution(keymap, targets):
    answer = []
        
    for i in targets:
        count = 0
        
        for j in i:
            idx_list = []
            not_list = []
            
            for k in keymap:                        # 해당 입력해야하는 키가 각 자판기에 인덱스 위치 값을 저장하여 최소 값을 넣어서 최소한의 입력으로 유도했다.
                if j in k:
                    idx_list.append(k.index(j))
                if j not in k:
                    not_list.append(-1)
            
            if len(not_list) == len(keymap):        # 각 자판기 모두 해당 키가 없으면 -1이 되므로 이를 처리해주는 것까지 해줘야 한다.
                count = 0
                break
            
            if len(idx_list) > 0:
                count += min(idx_list)+1
                
        if count == 0:
            answer.append(-1)
        else:
            answer.append(count)
    
    
    return answer