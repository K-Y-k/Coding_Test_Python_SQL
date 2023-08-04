# 시도한 방식
# S, D, T의 각 케이스일 때 그 안에서 *, #을 적용하려고 했지만 잘 안풀림 

def solution(dartResult):
    answer = 0
    score = 0
    dartResult_list=[]
    
    for i in dartResult:
        dartResult_list.append(i)
    
    for i, value in enumerate(dartResult_list):
        if value == 'S':
            if dartResult[i+1] == '*':
                score *= 2
                score += int(dartResult[i-2])*2
            elif dartResult[i+1] == '#':
                score -= int(dartResult[i-1])
            else:
                score += int(dartResult[i-1])
        elif value == 'D':
            if dartResult[i+1] == '*':
                score *= 2
                score += (int(dartResult[i-2])**2)*2
            elif dartResult[i+1] == '#':
                score -= int(dartResult[i-1])**2
            else:
                score += int(dartResult[i-1])**2
        elif value == 'T':
            if dartResult[i+1] == '*':
                score *= 2
                score += (int(dartResult[i-2])**3)*2
            elif dartResult[i+1] == '#':
                score -= int(dartResult[i-1])**3
            else:
                score += int(dartResult[i-1])**3

            
    return answer



# 처음부터 각 케이스로 나누고 연산한 것을 리스트에 넣어두고 처리하기
# *일 때 이전에 연산한 값이 변경되므로 각 연산한 것을 리스트로 담는 것이 유리하다.

def solution(dartResult):
    answer = 0
    num = ''
    score = []                               # *일 때 이전에 연산한 값이 변경되므로 각 연산한 것을 리스트로 담는 것이 유리하다.
    
    for i in dartResult:
        if i.isdigit():                      
            num += i                         # 문자열이므로 숫자가 2자리일 수도 있으므로 이어붙이게 함
        elif i == 'S':
            score.append(int(num))
            num = ''                         # 연산을 처리했으므로 초기화 잊지 말기
        elif i == 'D':
            score.append(int(num)**2)
            num = ''
        elif i == 'T':
            score.append(int(num)**3)
            num = ''
        elif i == '*':
            if len(score) == 1:              # 제일 연산 값에 *이 올 수 있다고 했으므로 따로 케이스 처리
                score[0] *=2
            else:
                score[-2] *= 2
                score[-1] *= 2
        elif i == '#':
            score[-1] *= -1
            
    answer = sum(score)
            
    return answer

