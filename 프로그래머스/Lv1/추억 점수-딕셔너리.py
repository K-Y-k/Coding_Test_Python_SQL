# 딕셔너리에 값을 넣어 놓고
# 각 루프를 돌 때 딕셔너리에 있는 값을 합산하고 적용한 것이다.


def solution(name, yearning, photo):
    answer = []
    yearning_dic = {}
    
    
    for i, value in enumerate(name):           # 딕셔너리에 값을 넣어 놓는다.
        if value not in yearning_dic:
            yearning_dic[value] = yearning[i]
            

    for i in photo:                            # 각 루프를 돌 때 딕셔너리에 있는 값을 합산하고 적용한 것이다.
        temp = 0 
        
        for j in i:
            if j in yearning_dic:
                temp += yearning_dic[j]
                
        answer.append(temp)
        
    
    return answer