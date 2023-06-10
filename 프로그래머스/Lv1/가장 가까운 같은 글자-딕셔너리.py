# 문제에서 왼쪽부터 읽어나간다고 했으므로 
# 즉, 1. 현재 위치에서 읽은 문자에서부터 왼쪽으로 해당 문자가 없으면 -1
#     2. 왼쪽에 있으면 현재 위치에서 그 위치까지의 간격을 나타내면 된다.
 

def solution(s):
    answer = []
    word_dic = {}                                 # 비교 대상의 문자와 그 문자의 위치를 저장할 딕셔너리
    
    for i, value in enumerate(s):
        if value not in word_dic:                 # 1. 현재 위치에서 읽은 문자에서부터 왼쪽으로 해당 문자가 없으면 -1을 넣고
            answer.append(-1)                     #    -1을 넣고 
            word_dic[value] = i                   #    딕셔너리에 해당 문자와 현재 위치를 넣어준다.

        else:                                     # 2. 왼쪽에 있으면 
            answer.append(i - word_dic[value])    #    현재 위치에서 그 위치까지의 간격(현재 위치 - 딕셔너리에 저장된 왼쪽에 있는 같은 문자의 위치)을 넣고
            word_dic[value] = i                   #    위치를 현재 문자의 위치로 새로 갱신한다.
        
    
    return answer