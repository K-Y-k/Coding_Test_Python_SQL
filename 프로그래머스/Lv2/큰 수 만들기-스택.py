# 내가 푼 방식 : 실행초과
# k개를 제거할 때까지 무한반복하여 
# 현재 위치 값이 다음 위치 값보다 크고 최대 값 설정한 값보다 크면 그 위치이전까지 값과 길이와 최대 값을 임시 변수들에 저장해놓고
# for 루프가 조회 완료되었으면 최신화한 임시 변수들에서 적용해가는 방식을 했지만 결국 실행초과로 실패

def solution(number, k):
    answer = ''
        
    count = 0
    max_temp = 0
        
    while count < k:
        for i, value in enumerate(number):
            if i > 0 and i < len(number)-1 and int(number[i]) > int(number[i+1]):
                a = number[i:i]

                if len(a) + count <= k and int(value) > max_temp: # 현재 위치 값이 다음 위치 값보다 크고 최대 값 설정한 값보다 크면 그 위치이전까지 값과 길이와 최대 값을 임시 변수들에 저장해놓고
                    max_temp = int(value)
                    temp = a
                    temp_count = len(temp)

            elif i == len(number)-1:                              # for 루프가 조회 완료되었으면 최신화한 임시 변수들에서 적용해가는 방식을 했지만 결국 실행초과로 실패
                count = temp_count
                number = number.replace(temp, '', 1)
                break
        

    return answer



# 스택을 활용한 방식
# 스택에 들어오는 최종 결과는 가장 큰 숫자들만 오는 곳이고
# 하나씩 숫자를 조회할 때 스택에 이미 값이 있으면 스택의 모든 값을 비교한다.
# 최근 들어온 것 순서로 비교하여 현재 숫자가 더 크면 스택에 담은 작은 것은 지워지고 그 숫자를 제거했으므로 제거 카운팅을 최신화해준다.

# 예외로 number문자가 오름차순으로 되어있어 k가 소진되지 않고 남아있을 경우
# 스택의 최근 기준으로 k를 모두 소진시키기 위해 남으 k만큼 제거해준다. 

def solution(number, k):
    answer = ''
    stack = []
    
    for i in number:
        while stack and stack[-1] < i and k > 0:      # 하나씩 숫자를 조회할 때 스택에 이미 값이 있으면 스택의 모든 값을 비교한다.
            k -= 1                                    # 최근 들어온 것 순서로 비교하여 현재 숫자가 더 크면 스택에 담은 작은 것은 지워지고 그 숫자를 제거했으므로 제거 카운팅을 최신화해준다.
            stack.pop()
        
        stack.append(i)
    
    if k > 0:                                         # 예외로 number문자가 오름차순으로 되어있어 k가 소진되지 않고 남아있을 경우
        answer = ''.join(stack[:len(stack)-k])        # 스택의 최근 기준으로 k를 모두 소진시키기 위해 남으 k만큼 제거해준다. 
    else:
        answer = ''.join(stack)
        
    
    return answer