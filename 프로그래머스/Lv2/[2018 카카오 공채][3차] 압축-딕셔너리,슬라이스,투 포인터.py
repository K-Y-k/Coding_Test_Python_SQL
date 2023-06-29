# 내가 푼 방식 : 하나의 테스트 케이스 일부만 맞게 억지로 만듦...

def solution(msg):
    answer = []
    
    dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for i, value in enumerate(msg):
        temp = {}
        for j in dic:
            if value[0] in j[0] and j not in temp:
                temp[j] = 1
        
        a = sorted(temp, reverse=True)
        index = dic.index(a[0])
        
        if a[0] in dic:
            answer.append(index+1)
            if index < len(msg)-1 and msg[index:index+2] not in dic:
                dic.append(msg[index:index+2])
        else:
            dic.append(value)
            
    return answer



# [현재글자 + 다음글자]가 사전에 있을 때 또는 사전에 없을때 인덱스가 어떻게 변하는지 파악하는게 핵심

def solution(msg):
    answer = []
    
    # 사전 초기화 A~Z
    dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

    w = 0                                      # 인덱스 초기화
    c = 0

    while True:
        c += 1	                               # c의 위치를 증가

        if c == len(msg):	                   # c의 위치가 끝까지 도달했으면 마지막 단어이므로
            answer.append((dic[msg[w:c]]))     # 현재 단어를 출력하는 정답에 넣고
            break                              # 반복 탈출
        
                
        if msg[w:c+1] not in dic:              # [현재글자+다음글자]가 사전에 없다면
            dic[msg[w:c+1]] = len(dic) + 1     # 사전에 추가하고
            answer.append(dic[msg[w:c]])       # 정답에 넣어주고
            w = c	                           # 현재글자를 다음글자로 옮겨줌
            
        
        # 만약 [현재글자+다음글자]가 사전에 있다면 w의 값은 변하지 않고 c의 값만 1씩 증가한다.
    

    return answer