# 옹알이 목록의 단어를 구별처리하는 문자로 변환하고
# 마지막에 구별처리한 문자를 공백으로 바꾸어 만약 비어있다면 카운팅 처리하였다. 

# 주의점
# 1) replace는 다른 변수에 다시 저장해야하고 replace를 아래처럼 .을 붙여 연속으로 사용가능하다.
# 2) 구별하는 문자로 먼저 바꾸어줘야한다. 만약 이를 무시하고 공백으로 바꾸면 공백으로 인해 이어붙여진 단어가 옹알이 목록에 포함되면 다른 결과가 된다. 


def solution(babbling):
    answer = 0
    
    for i in babbling:
        i = i.replace("aya", "*").replace("ye", "*").replace("woo", "*").replace("ma", "*") # 옹알이 목록의 단어를 구별처리하는 문자로 변환하고
        i = i.replace("*", "")                                                              # 마지막에 구별처리한 문자를 공백으로 바꾸어
        
        if not i:                                                                           # 만약 비어있다면 카운팅 처리하였다. 
            answer += 1
    
    
    return answer