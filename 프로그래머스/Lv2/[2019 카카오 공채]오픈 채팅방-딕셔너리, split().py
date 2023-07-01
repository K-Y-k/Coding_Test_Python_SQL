# 내가 푼 방식
# 처음 기록 조회에서는 각 단어를 쪼개서 해당 uid를 딕셔너리에 최신화 시켜놓은 뒤
# 다시 기록을 조회하여 각 단어를 쪼개서 uid의 값의 최신 이름을 넣게 하였다.

def solution(record):
    answer = []
    key = {}
    
    for i in record:                                    # 처음 기록 조회에서는 각 단어를 쪼개서 해당 uid를 딕셔너리에 최신화 시켜놓은 뒤
        if i[0] == "E":
            s = i.split(" ")
            key[s[1]] = s[2]
        elif i[0] == "C":
            s = i.split(" ")
            key[s[1]] = s[2]
            
    for i in record:                                    # 다시 기록을 조회하여 각 단어를 쪼개서 uid의 값의 최신 이름을 넣게 하였다.
        if i[0] == "E":
            s = i.split(" ")
            message = key[s[1]] +"님이 들어왔습니다."
            answer.append(message)
        elif i[0] == "L":
            s = i.split(" ")
            message = key[s[1]] +"님이 나갔습니다."
            answer.append(message)
        
    
    return answer


# 개선해야 할 것 : 먼저 쪼개고난 후 각 단어로 비교하자
for i in record:
     s = i.split(" ")

     if s[0] == "Enter":
         key[s[1]] = s[2]
     elif s[0] == "Change":
        key[s[1]] = s[2]

for i in record:
     s = i.split(" ")
     if s[0] == "Enter":
        message = key[s[1]] +"님이 들어왔습니다."
        answer.append(message)
     elif s[0] == "Leave":
        message = key[s[1]] +"님이 나갔습니다."
        answer.append(message)