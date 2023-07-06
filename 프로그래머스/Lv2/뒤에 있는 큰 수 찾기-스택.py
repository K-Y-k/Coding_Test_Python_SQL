# 내가 푼 방식 : 일부 테스트 케이스 시간초과
# 이중 루프로 현재 가져온 숫자에서 다음 숫자부터 차례로 비교하여 
# 큰수가 있으면 넣어주고 모두 조회해도 없으면 -1을 넣었다.
# 하지만 문제에서 numbers의 최대 개수가 1000000개이므로 이중 루프면 시간 초과가 될 수 있다.

def solution(numbers):
    answer = []
            
    for i, value in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            if value < numbers[j]:
                answer.append(numbers[j])
                break
        else:
            answer.append(-1)
    

    return answer



# 스택으로 푼 방식
# 문제에서 가장 가까운 큰 수라고 했으므로 스택이 떠올라아야 한다!
# 스택에 담고 while문의 조건이 맞을 경우만 루프를 돌아 스택에서 꺼내와 정답에 넣어주었다.
# 다음 숫자가 작은 수이면 계속 스택에 쌓이고 큰 숫자가 나오면 결국 쌓였던 스택의 숫자보다도 다음 큰 수이기에 각 위치의 값에 저장했다.   

def solution(numbers):
    answer = [-1] * len(numbers)                     # 스택에 쌓이는 방식이므로 각 위치에 직접 저장해주어야하므로 개수만큼 초기화했고 
                                                     # 또한 큰 숫자가 없어 끝까지 스택에 계속 남아있으면 -1을 반환해야하므로 처음 초깃값을 -1로 한것이다.
    stack = []
    
    for i, value in enumerate(numbers):            
        while stack and numbers[stack[-1]] < value:  # while문의 조건이 맞을 경우만 루프를 돌아
            answer[stack.pop()] = value              # 스택에서 꺼내와 정답에 넣어주었다.
        
        stack.append(i)

    
    return answer