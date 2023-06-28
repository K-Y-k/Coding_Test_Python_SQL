# 내가 푼 방식 : 다중 중복 처리를 못함
# 1. 대소문자를 구분하지 않으므로 처음에 lower로 통일시키고 2개 연속된 문자가 특수문자가 아닌 것만 각자의 리스트에 저장하고
# 2. 교집합, 합집합을 각각 구하고
# 3. 연산을 처리한다.

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()                                  # 대소문자를 구분하지 않으므로 처음에 lower로 통일시키고
    str2 = str2.lower()
    
    str1_list = []
    str2_list = []
    
    for i in range(0, len(str1)-1):                      # 2개 연속된 문자가 특수문자가 아닌 것만 각자의 리스트에 저장하고
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i:i+2])
    
    for i in range(0, len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i:i+2])
    
    
    set_list = []
    sum_list = []
    
    for i in str1_list:
        sum_list.append(i)
        
        for j in str2_list:
            if i == j:
                set_list.append(j)
            
            if j not in sum_list:
                sum_list.append(j)
    
    if len(set_list) > 0:
        J = len(set(set_list)) / len(set(sum_list))
    else:
        J = 1
    
    answer = int(J * 65536)
    
    
    return answer



# 다중 중복처리까지 완료한 방식

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_list = []
    str2_list = []
    
    for i in range(0, len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i:i+2])
    
    for i in range(0, len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i:i+2])
    
    
    set_list = []
    sum_list = []
    
    for i in (set(str1_list+str2_list)):                 # 2. 교집합, 합집합을 각각 구하고
        str1_count = str1_list.count(i)
        str2_count = str2_list.count(i)
        m = min(str1_count,str2_count)
        
        set_list.append(m)
    
    for i in (set(str1_list+str2_list)):
        str1_count = str1_list.count(i)
        str2_count = str2_list.count(i)
        m = max(str1_count,str2_count)
        
        sum_list.append(m)


    if len(set_list) > 0:                                # 3. 연산을 처리한다.
        J = sum(set_list) / sum(sum_list)
    else:
        J = 1
    
    answer = int(J * 65536)
    
    
    return answer