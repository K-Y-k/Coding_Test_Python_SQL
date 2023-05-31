# 문제의 각 단계별로 진행해주면 된다.


def solution(new_id):
    answer = ''
    
    for i in new_id:
        # 1단계: 모든 대문자를 대응되는 소문자로 치환합니다.
        if i.isalpha():
            i = i.lower()
            
        # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
        if i.isdigit() or i.isalpha() or i in '-_.': # 부족 1) i in '-_.' 부분 부족했음
            answer += i

    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while '..' in answer:                            # 부족 2) while '..' in answer 부분이랑 replace 활용이 부족했음 
        answer = answer.replace('..', '.')
    
    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if answer and answer[0] == '.':                  # 부족 3) answer가 있는지도 확인해야한다.
        answer = answer[1:]
    if answer and answer[-1] == '.':                 # 부족 4) 변수[-1]은 마지막 값이지만
        answer = answer[0:-1]                        #         변수[0:-1]로 범위로 지정일 때는 마지막의 앞의 값까지이다.  
        
    # 5단계: 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if answer == '':
        answer += 'a'
    
    # 6단계: 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #        만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(answer) >= 16:
        answer = answer[0:15]
        
        if answer[-1] == '.':                      # 15자리로 강제로 줄이면서 '.'이 마지막이 될 수 있으므로 마지막 값이 '.'인 것을 한번 더 확인해야한다.
            answer = answer[0:-1]
        
    # 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
        
    
    return answer