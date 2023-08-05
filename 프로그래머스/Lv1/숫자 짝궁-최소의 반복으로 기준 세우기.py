# 시도한 방식 : 일부 테스트 케이스 실행초과 발생
# X를 기준으로 조회하면서 X의 숫자가 Y의 숫자에 있으면 공통 숫자 리스트에 넣고 Y의 공통 숫자를 중복 발생하지 않게 지워주었다.
# 저장된 공통 숫자 리스트를 최대 값 순서로 넣었고 
# 빈 공백일 때랑 0이 연속으로 와서 0으로 표현해야하는 경우도 처리하였다.

def solution(X, Y):
    answer = ''
    common_num = []
    
    for i in X:                              # X를 기준으로 조회하면서
        if i in Y:                           # X의 숫자가 Y의 숫자에 있으면
            common_num.append(int(i))        # 공통 숫자 리스트에 넣고
            Y = Y.replace(i,'',1)            # Y의 공통 숫자를 중복 발생하지 않게 지워주었다.
            
    for _ in range(len(common_num)):         # 저장된 공통 숫자 리스트를 최대 값 순서로 정답에 넣었고 
        answer += str(max(common_num))
        common_num.remove(max(common_num))
    
    if len(answer) == 0:                     # 정답이 빈 공백일 때랑
        answer = '-1'
    elif answer[0] == '0':                   # 0이 연속으로 와서 0으로 표현해야하는 경우도 처리
        answer = '0'
    
    return answer



# 시간초과를 방지하기 위해 기준을 올 수 있는 숫자로 조회!
# 0~9의 숫자로 조회하여 해당 숫자가 X, Y에 같이 있으면 
# X와 Y에서 해당 숫자가 몇개 있는지도 같이 카운팅하고 각 카운팅 숫자중 적은 수(=공통 최대의 수)로 
# 그 공통 수 만큼 반복해서 공통 숫자 리스트에 넣었다.

def solution(X, Y):
    answer = []
    
    for i in range(0, 10):                                         # 시간초과를 방지하기 위해 기준을 올 수 있는 0~9의 숫자로 조회!
        if str(i) in X and str(i) in Y:                            # 해당 숫자가 X, Y에 같이 있으면 공통 숫자 리스트에 넣었다
            for _ in range(min(X.count(str(i)), Y.count(str(i)))): # X와 Y에서 해당 숫자가 몇개 있는지도 같이 카운팅하고 각 카운팅 숫자중 적은 수(=공통 최대의 수)로 
                answer.append(str(i))                              # 그 공통 수 만큼 반복해서 공통 숫자 리스트에 넣었다.
                
    answer.sort(reverse=True)                                      # 최대 값으로 표현하기 위해 내림차순으로 정렬
    
    if len(answer) == 0:
        answer = '-1'
    elif answer[0] == '0':
        answer = '0'
    else:
        answer = ''.join(answer)
    
    return answer

