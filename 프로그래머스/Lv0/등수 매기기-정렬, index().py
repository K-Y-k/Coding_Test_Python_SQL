# 내가 푼 방식
# 평균 값을 평균 리스트에 넣어주고
# 평균 리스트의 현재 값과 다른 값들을 비교하며 순위를 일일히 카운팅하여 넣어주었다. 

def solution(score):
    answer = []
    avg_list = []
    
    for i in score:                                # 평균 값을 평균 리스트에 넣어주고
        temp_avg = (i[0] + i[1]) / 2
        avg_list.append(temp_avg)
    
    
    for i in range(len(avg_list)):                 # 평균 리스트의 현재 값과 다른 값들을 비교하며 순위를 일일히 카운팅하여 넣어주었다. 
        temp = len(avg_list)
        
        for j in range(len(avg_list)):
            if i != j:
                if avg_list[i] >= avg_list[j]:
                    temp -= 1
                
        answer.append(temp)
    
    
    return answer



# 정렬 방식
# 어차피 순위를 매기는 것이니 평균을 정확히 구할 필요는 없어 더하기만 한 값을 넣고
# 평균 리스트를 큰 수부터 내림차순으로 정렬하여
# 기존 점수 리스트의 합과 동일한 평균 리스트의 값의 인덱스를 등수로 넣었다. 

def solution(score):
    answer = []
    avg_list = []
    
    for i in score:                                 # 어차피 순위를 매기는 것이니 평균을 정확히 구할 필요는 없어 더하기만 한 값을 넣고
        temp_avg = sum(i)
        avg_list.append(temp_avg)
        
    avg_list.sort(reverse=True)                     # 평균 리스트를 큰 수부터 내림차순으로 정렬하여
    
    for i in score:                                 # 기존 점수 리스트의 합과 동일한 평균 리스트의 값의 인덱스를 등수로 넣었다. 
        answer.append(avg_list.index(sum(i))+1)
    
    
    return answer