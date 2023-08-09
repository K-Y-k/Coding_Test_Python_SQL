# 내가 푼 방식
# 각 성격에 대한 점수를 한쌍으로 넣은 딕셔너리를 만들었고
# 각 점수에 해당하는 성격에 카운팅 해주고
# 비교해야 하는 성격들을 서로 비교하여 큰 값인 성격으로 넣어주었다.

def solution(survey, choices):
    answer = ''
    
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}    # 각 성격에 대한 점수를 한쌍으로 넣은 딕셔너리를 만들었고
    
    for i, value in enumerate(survey):                                # 각 점수에 해당하는 성격에 카운팅 해주고
        if choices[i] == 4:
            continue
        elif choices[i] == 1 or choices[i] == 2 or choices[i] == 3:
            dic[value[0]] += 4 - choices[i]
        else:
            dic[value[1]] += choices[i]-4
        
        # if choices[i] == 1:
        #     dic[value[0]] += 3
        # elif choices[i] == 2:
        #     dic[value[0]] += 2
        # elif choices[i] == 3:
        #     dic[value[0]] += 1
        # elif choices[i] == 5:
        #     dic[value[1]] += 1
        # elif choices[i] == 6:
        #     dic[value[1]] += 2
        # elif choices[i] == 7:
        #     dic[value[1]] += 3
    
    
    key = [i for i in dic.keys()]
    
    for i in range(0, 8, 2):                                          # 비교해야 하는 성격들을 서로 비교하여 큰 값인 성격으로 넣어주었다.
        if dic[key[i]] >= dic[key[i+1]]:
            answer += key[i]
        else:
            answer += key[i+1]

    # if dic['R'] >= dic['T']: answer += 'R'                            
    # else: answer += 'T'
    
    # if dic['C'] >= dic['F']:answer += 'C'
    # else: answer += 'F'
        
    # if dic['J'] >= dic['M']: answer += 'J'
    # else: answer += 'M'
        
    # if dic['A'] >= dic['N']:answer += 'A'
    # else: answer += 'N'
    
    return answer