# 각 받아온 오늘의 날짜, 텀 기간, 각 개인정보를 slpit()으로 쪼개고 난 후 
# 텀을 더한 날짜를 서로 비교해가며 유효한지 검사했다. 


def solution(today, terms, privacies):
    answer = []

    to_year, to_month, to_day = map(int, today.split('.'))    # 오늘 날짜 연, 월, 일 분리
    
    term_alpha_list = []                                      # 텀 알파벳 담기
    term_num_list = []                                        # 텀 기간 담기
    
    for i in range(len(terms)):                               # 텀을 분리한 후 각 알파벳, 기간에 따로 담아두기  
        term_alpha, term_num = map(str, terms[i].split())
        term_alpha_list.append(term_alpha)
        term_num_list.append(term_num)
    
    for i in range(len(privacies)):                          # 각 개인정보 반복하여 
        date, grade = map(str, privacies[i].split())         # 날짜, 텀 등급을 따로 분리
        year, month, day = map(int, date.split('.')) 
        
        for j in range(len(term_alpha_list)):                # 받아온 개인정보의 등급과 텀의 알파벳을 비교해 
            if grade == term_alpha_list[j]:                  # 맞으면 그 인덱스의 텀 기간을 더하고
                month += int(term_num_list[j])
                while True:                                  # 무한 반복으로
                    if month <= 12:                          # 12월이하가 될 때까지
                        break
                    year += 1                                # 연도를 갱신해준다.
                    month -= 12
                    
        if year > to_year :                                  # 개인정보의 유효 연도가 오늘의 연도보다 크다면 넘어가고
            continue                                         
        elif year == to_year :                               # 연도가 같으면
            if month > to_month :                            # 개인정보의 유효 달이 오늘의 달보다 크면 넘어가고
                continue
            elif month == to_month :                         # 달이 같을 때
                if day > to_day :                            # 개인정보의 유효 일이 오늘의 일보다 크면 넘어가고
                    continue
                     
        answer.append(i+1)                                   # 위 조건들이 아닐 때 파기 대상으로 답에 넣는다.
       
    return answer