# 내가 푼 방식 : 일부 테스트 케이스 실패
# 발음할 수 있는 것을 하나씩 조회해서 발음할 수 있는 단어가 있으면 1개씩 지우면서 최근 발음 단어에 저장해서 
# 발음할 수 있는 단어이면서 최근 발음 단어가 아니게 조건을 처리했다.

def solution(babbling):
    answer = 0
    bablbling_list = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:
        recent_babling = ''
        
        while True:                                   # 하나씩 지워나갔기에 같은 발음이 또 있을 수 있으므로 무한 루프로 했다..
            for b in bablbling_list:                  # 발음할 수 있는 것을 하나씩 조회해서
                if b in i and b != recent_babling:    # 발음할 수 있는 단어이면서 최근 발음 단어가 아니면
                    i = i.replace(b, '', 1)           # 그 단어를 하나 지우고
                    recent_babling = b                # 최근 발음 단어에 최신화

                    if i == '':                       # 빈문자열이 될경우 카운팅하면서 무한반복 탈출
                        answer += 1
                        break
            else:                                     # 위 발음 가능 리스트를 끝까지 조회했음에도 없으면 무한반복 탈출
                break
            
    
    return answer



# 하나씩 지워나가는 것이 아닌
# 각 발음 가능 리스트의 단어를 한번 조회할 때 해당 단어를 모두 지우게 처리하면 된다.
# 주의점 1) 연속되는 같은 발음 가능 단어가 있으면 안되므로 해당 조건도 추가해야함
#        2) 지워줄 때 ''이 아닌 ' '공백으로 변경해야 이어붙여저서 새로운 단어가 생성되지 않도록 해야 한다.

def solution(babbling):
    answer = 0
    bablbling_list = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:        
        for b in bablbling_list:                   # 각 발음 가능 리스트의 단어를 한번 조회할 때
            if b in i and b*2 not in i:            # 발음할 수 있는 단어가 있으면서 연속되는 같은 발음 가능 단어가 없으면
                i = i.replace(b, ' ')              # 해당 단어를 모두 지우게 처리 
                                                   # ' '공백을 변경해야 이어붙여저서 새로운 단어가 생성되지 않는다.

                if i.isspace():                    # 여러 공백이 띄워져 있으므로 ==''이 아닌 isspace()로 구분해야한다!  
                    answer += 1
            
    return answer