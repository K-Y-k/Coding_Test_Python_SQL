# 내가 푼 방식 : 무한 루프 발생
# 각 자리가 같으면 temp 리스트에 넣어두고 모두 적용된 temp에서 replace를 ''로 지워주는 작업을 진행하려고 했지만
# 무한 루프에서 탈출이 잘 되지 않았다.

def solution(s):
    answer = 0

    while True:
        for i in range(len(s)-1):
            temp = []

            for j in range(i+1, len(s)):
                if j == i+1:
                    temp.append(s[j])
                elif temp[0] == s[j]:
                    temp.append(s[j])
                else:
                    break

            if len(temp) > 1:
                break

        if len(temp) > 1:
            join_temp = "".join(temp)
            s.replace(join_temp, '')
        elif len(temp) == 0:
            answer = 1
            break
        elif len(temp) == 1:
            break
            

    return answer



# 스택의 활용
# 스택에 담아두고 제일 최근에 담은 것과 비교하면서 같으면 지워나가면 결국 문제에서 원하는 결과가 나온다.

def solution(s):
    answer = -1
    stack = []
    
    for i in s:
        if len(stack) == 0:   # 아직 담아진 것이 없을 때 
            stack.append(i)
        elif stack[-1] == i:  # 최근에 담긴 것과 비교하여 같으면 스택의 그 값을 지워주기
            stack.pop()
        else:                 # 다르면 값을 넣고 진행
            stack.append(i)
    
    if len(stack) == 0:       # 스택이 비어있으면 모두 짝이 있어 지워진 것이므로 1
        answer = 1
    else:                     # 스택이 비어있지 않으면 짝이 나오지 않은 것이 있어 0
        answer = 0

    return answer