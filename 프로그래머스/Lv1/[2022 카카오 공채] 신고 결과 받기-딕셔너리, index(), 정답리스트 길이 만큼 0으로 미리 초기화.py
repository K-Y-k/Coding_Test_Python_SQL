# 내가 시도한 방식 : 시간 초과
# 각 아이디에 해당하는 신고 카운팅을 한 쌍의 딕셔너리로 생성하고
# 중복되는지 검사하기 위한 리스트를 만들어서 새로운 신고가 들어왔을 때 중복 리스트에 넣고 그다음 부터 중복리스트의 값과 일치하는지 검사하는 방식을 택했다.
# 그렇게 카운팅한 후 id 리스트와 신고 리포트를 2중 루프하여 각 id와 신고당한id의 신고당한횟수 값이 맞으면 카운팅하여 정답에 넣었다. 

# 하지만 이렇게 중복 검사하는 방식과 이중 루프로 조회하는 곳이 있어 비효율적이라 시간초과가 발생한다.

def solution(id_list, report, k):
    answer = []
    
    distinct_list = []                        # 중복되는지 검사하기 위한 리스트 생성

    report_dic = {}                           # 각 아이디에 해당하는 신고 카운팅을 한 쌍의 딕셔너리로 생성하고
    for i in id_list:
        report_dic[i] = 0
    
    
    for i in report:    
        if i not in distinct_list:            # 새로운 신고가 들어왔을 때 
            distinct_list.append(i)           # 중복 리스트에 넣고

            a, b = i.split(' ')
            report_dic[b] += 1                # 신고 카운팅
            
    
    for i in id_list:                         # id 리스트와
        count = 0
        
        for j in report:                      # 신고 리포트를 2중 루프하여 각 id와 신고당한id의 신고당한횟수 값이 맞으면 카운팅하여 정답에 넣었다.
            a, b = j.split(' ')
            
            if report_dic[b] >= k and i == a: # 각 id와 신고당한 id의 신고 당한 횟수 값이 맞으면
                count += 1                    # 카운팅하여
                
        answer.append(count)                  # 정답에 넣었다.
    
    
    return answer



# 그래서 처음에 신고 리스트에 set으로 중복되는 신고를 처음부터 지워주고
# 2중 루프가 안되게 answer 리스트에 미리 길이 만큼 0으로 초기화해 두게 하여 id_list의 인덱스와 매칭시켜 
# 1중 루프로 카운팅하게 했다.

def solution(id_list, report, k):
    answer = [0] * len(id_list)              # 2중 루프가 안되게 answer 리스트에 미리 길이 만큼 0으로 초기화한다.
    report = list(set(report))               # 처음에 신고 리스트에 set으로 중복되는 신고를 처음부터 지워주고
    
    report_dic = {}
    for i in id_list:
        report_dic[i] = 0
    
    
    for i in report:
        a, b = i.split(' ')
        report_dic[b] += 1
            
            
    for i in report:                         # 1중 루프로 카운팅하게 했다.
        a, b = i.split(' ')
        
        if report_dic[b] >= k:            
            answer[id_list.index(a)] += 1    # 2중 루프가 안되게 answer 리스트에 미리 길이 만큼 0으로 초기화해 뒀기에 id_list의 인덱스와 매칭시켜 카운팅
    
    return answer