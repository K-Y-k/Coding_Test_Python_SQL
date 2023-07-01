# 내가 푼 방식
# 1.IN이 들어올 때는 In 딕셔너리에 차번호와 분단위인 현재 시간을 따로 저장해 두고
#   OUT이 들어올 때는 OUT의 분단위 시간과 In 딕셔너리의 같은 차번호의 분단위 시간을 뺀 것을 최종 결과 딕셔너리에 최신화 시켜주고 IN 딕셔너리의 해당 차번호와 시간을 제거
# 2.위 모든 루프를 조회한 후 IN 딕셔너리에 아직 존재하는 것이 있으면 23:59인 분단위에서 뺀 값을 최종 결과 딕셔너리에 최신화 시켜준고
# 3.최종 결과 딕셔너리의 최종 분에 주어진 요금 연산을 하여 정답에 추가해주었다. 

# 연산시 주의할 점은 각 분 단위로 나눈 시간을 올림처리하라고 했으므로 이 부분 주의

import math

def solution(fees, records):
    answer = []
    In_dic = {}
    result_dic = {}
    
    for i in records:                                     
        if "IN" in i:                                      # 1.IN이 들어올 때는 In 딕셔너리에 차번호와 분단위인 현재 시간을 따로 저장해 두고
            s = i.split(" ")
        
            time_s = s[0].split(":")
            time = int(time_s[0]) * 60 + int(time_s[1])
            In_dic[s[1]] = time
        elif "OUT" in i:                                   #   OUT이 들어올 때는 OUT의 분단위 시간과 In 딕셔너리의 같은 차번호의 분단위 시간을 뺀 것을 최종 결과 딕셔너리에 최신화 시켜주고 IN 딕셔너리의 해당 차번호와 시간을 제거
            s = i.split(" ")
        
            time_s = s[0].split(":")
            time = int(time_s[0]) * 60 + int(time_s[1])
            
            total_time = time-In_dic[s[1]]
            
            if s[1] in result_dic:
                result_dic[s[1]] += total_time
            else:
                result_dic[s[1]] = total_time
            
            In_dic.pop(s[1])
            
            
    if In_dic:                                             # 2.위 모든 루프를 조회한 후 IN 딕셔너리에 아직 존재하는 것이 있으면 23:59인 분단위에서 뺀 값을 최종 결과 딕셔너리에 최신화 시켜준고
        for i in In_dic:
            time = 23*60+59 - In_dic[i]
            if i in result_dic:
                result_dic[i] += time
            else:
                result_dic[i] = time
                
        In_dic.clear()                                     # 모두 처리했으므로 비우기
    
    
    result_dic = dict(sorted(result_dic.items()))          # In일 때 제거해주면서 했기에 문제에서는 차번호 순으로 출력을 원하므로 최종 정렬 처리 
    
    for i in result_dic:                                   # 3.최종 결과 딕셔너리의 최종 분에 주어진 요금 연산을 하여 정답에 추가해주었다. 
        if result_dic[i] > fees[0]:
            price = fees[1] + (math.ceil((result_dic[i]-fees[0])/fees[2])) * fees[3]  # 분단위 구할 때 올림 처리해야한다! 
        else:
            price = fees[1]
        
        answer.append(price)
    return answer