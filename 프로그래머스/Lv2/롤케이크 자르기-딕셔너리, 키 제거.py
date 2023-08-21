# 내가 푼 방식 : 일부 테케 제외하고 모두 시간 초과
# 주어진 topping길이를 차례로 반복하면서 
# 현재 차례의 인덱스를 기준으로 각 슬라이싱한 케이크 2개를 set으로 중복을 없애 다른 종류의 개수로 비교하였지만
# 계속 반복할 때마다 해당 케이크를 초기화를 하는 과정에서 시간초과가 발생하였다.

def solution(topping):
    answer = 0
    
    for i in range(1, len(topping)):                    # 주어진 topping길이를 차례로 반복하면서 
        tmp1 = topping[:i]                              # 현재 차례의 인덱스를 기준으로 각 슬라이싱한 케이크 2개를 만들고
        tmp2 = topping[i:]
        
        if len(set(tmp1)) == len(set(tmp2)):            # set으로 중복을 없애 다른 종류의 개수로 비교하였지만
            answer += 1                    
                                                        # 계속 반복할 때마다 해당 케이크를 초기화를 하는 과정에서 시간초과가 발생하였다.
        
    return answer



# 딕셔너리를 활용한 방식
# 딕셔너리는 데이터에 접근하는 속도가 빠르기에 시간초과가 발생하지 않는 것이다.
# 전체 토핑을 딕셔너리로 만들어 주었고
# 비교 대상 토핑을 전체 토핑에서 하나씩 가져오면서 전체 토핑 딕셔너리에 해당 값을 차감하고 0이 되면 해당 종류의 키를 제거해주었고
# 가져온 값을 비교 대상 토핑에 적용시켜
# 서로의 딕셔너리 길이를 비교하면 결국 종류의 개수를 비교하는 것이다.

def solution(topping):
    answer = 0
    
    topping_dic = {}
    tmp_topping_dic = {}
    
    for i in topping:                                    # 전체 토핑을 딕셔너리로 만들어 주었고
        if i not in topping_dic:
            topping_dic[i] = 1
        else:
            topping_dic[i] += 1
    
    
    for i in topping: 
        topping_dic[i] -= 1                              # 비교 대상 토핑을 전체 토핑에서 하나씩 가져오면서 전체 토핑 딕셔너리에 해당 값을 차감하고
        if topping_dic[i] == 0:                          # 0이 되면 해당 종류의 키를 제거해주었고
            topping_dic.pop(i)
            # del topping_dic[i]
        
        if i not in tmp_topping_dic:                     # 가져온 값을 비교 대상 토핑에 적용시켜
            tmp_topping_dic[i] = 1
        else:
            tmp_topping_dic[i] += 1
                
        if len(topping_dic) == len(tmp_topping_dic):     # 서로의 딕셔너리 길이를 비교하면 결국 종류의 개수를 비교하는 것이다.
            answer += 1
        
        
    return answer