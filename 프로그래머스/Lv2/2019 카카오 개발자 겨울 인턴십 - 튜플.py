def solution(s):
    answer = []
    
    s = s[2:-2]                         # 튜플 슬라이스로 처음의 {{ }}부분을 제거
    s = s.split("},{")                  # split()으로 },{을 제거해주고 
    
    s.sort(key = len)                   # 길이 오름차순으로 정렬
    
    for i in s:
        s_x = i.split(',')              # 을 제거해 숫자만 남겨
        
        for j in s_x:
            if int(j) not in answer:    # 해당 숫자가 없으면
                answer.append(int(j))   # 위 정렬 순서대로 숫자를 답에 넣어준다.
    
    return answer