# 내가 푼 방식
# 1. 대진표가 1<->2 3<->4와 같이 바로 옆 사람끼리 붙으므로 현재 인덱스와 다음 인덱스를 겨루는 방식을 고안했다.
# 2. A, B의 사람을 구분하기 위해 그 위치의 값을 A와 B로 표현하여 숫자가 아닌 문자일 경우는 무조건 승리한 리스트에 넣어 적용시켰다. 


def solution(n,a,b):
    answer = 0
    fight_list = []
    
    for i in range(1, n+1):          # A, B를 구분하기 위해 그 위치의 값을 A와 B로 넣음
        if i == a:
            fight_list.append('A')
        elif i == b:
            fight_list.append('B')
        else:
            fight_list.append(i)
            
    
    round_count = 0                  # 몇 라운드인지 카운트할 변수 선언
    
    while len(fight_list) > 1:       # 최종 승자 1명이 남을 때까지 반복
        round_count += 1             # 라운드 카운팅
        temp = []                    # 현재 라운드에서 승리한 사람만 넣을 리스트 선언
        
        for i in range(0, len(fight_list), 2):                                          # 현재 인덱스와 다음 인덱스를 비교할 것이므로 2칸씩 뛰어넘음
            if str(fight_list[i]).isalpha() and str(fight_list[i+1]).isalpha():         # 만약 둘 다 A,B이면 문제에서 원하는 라운드 반환 
                return round_count
            else:
                if str(fight_list[i]).isalpha():                                        # 현재 인덱스만 A,B이면 현재 인덱스가 무조건 승리해야하므로 현재 인덱스의 값만 승리 리스트에 넣음
                    temp.append(fight_list[i])                                  
                elif str(fight_list[i+1]).isalpha():                                    # 다음 인덱스만 A,B이면 다음 인덱스가 무조건 승리해야하므로 다음 인덱스의 값만 승리 리스트에 넣음
                    temp.append(fight_list[i+1])
                elif str(fight_list[i+1]).isdigit() and str(fight_list[i+1]).isdigit(): # 둘 다 숫자이면 아무나 한명 승리 리스트에 넣어도 됨
                    temp.append(fight_list[i])
        
        fight_list = temp                                                               # 승리 리스트의 값으로 적용하기
    
    

    return answer