# 시도한 방식 : 일부 테스트 케이스 실패
# 딕셔너리에 키는 문자, 값은 문자 카운팅한 값으로 했다.
# 기준 값 x와 x외의 문자를 모두 한 곳으로 나눈 것이었는데 착각했다.

def solution(s):
    answer = 0
    s_dic = {}
    tmp = ''

    for i in s:
        tmp += i

        if i not in s_dic:
            s_dic[i] = 1
        else:
            s_dic[i] += 1

        if len(s_dic) > 1:
            for j in s_dic:
                if i != j and s_dic[i] == s_dic[j]:
                    s=s.replace(tmp, '', 1)
                    tmp = ''
                    s_dic = {}
                    answer += 1
                    break
                    
    if len(s) > 0:
        answer += 1
            
    return answer



# x와 x외의 문자를 한곳에로 2군데의 카운트로 나누어서
# 두 카운트가 같을 때 정답 카운팅을 하고 그때 하나의 문자를 x로 기준 값을 잡아서
# x일 때의 카운트와 그외 문자 카운팅을 처리한다.

def solution(s):
    answer = 0
    
    count1 = 0                 # x와 x외의 문자를 한곳에로 2군데의 카운트로 나누어서
    count2 = 0
    
    for i in s:
        if count1 == count2:   # 두 카운트가 같을 때
            answer += 1        # 정답 카운팅을 하고
            x = i              # 그때 하나의 문자를 x로 기준 값을 잡아서
        
        if x == i:             # x일 때의 카운트와 그외 문자 카운팅을 처리한다.
            count1 += 1
        else:
            count2 += 1
    
    
    return answer
