# 내가 시도해본 방식
# 루프 기준을 택배 주문 순서를 기준으로하여
# 스택으로 쌓는 벹트와 기존 컨테이너를 분리하여
# 기존 컨테이너의 숫자가 주문한 숫자와 같지 않으면 스택 벨트에 보관하게하고 이렇게 하려했지만..
# 기준을 이렇게 잡으면 해결할 수가 없었다.


# 무조건 스택에 넣은 다음 비교하는 방법
# 컨테이너가 1~5로 차례로 있으므로 루프를 해당 컨테이너 순서로 기준을 잡고 반복하여
# 현재 숫자를 스택에 무조건 넣은 다음 택배 상자 주문 순서와 스택의 최근 값이랑 같으면 스택에서 빼주면서 카운트를 올리고
# 해당 카운트가 곧 택배 상자 주문 순서의 인덱스와 동일하므로 이렇게 비교처리를 한 것이다. 

def solution(order):
    stack = []
    count = 0                                          # 택배 상자 주문 순서의 인덱스가 곧 문제에서 원하는 정답
    container_i = 1                                    # 컨테이너가 1~5로 차례로 있으므로 초깃값 1로 초기화
    
    while container_i < len(order) + 1:                # 해당 컨테이너 순서로 기준을 잡고 반복하여
        stack.append(container_i)                      # 현재 숫자를 스택에 무조건 넣은 다음
        
        if stack[-1] == order[count]:                  # 택배 상자 주문 순서와 스택의 최근 값이랑 같으면
            while stack and stack[-1] == order[count]: # 해당 카운트가 곧 택배 상자 주문 순서의 인덱스와 동일하므로 이렇게 비교처리를 한 것이다. 
                stack.pop()                            # 스택에서 빼주면서 
                count += 1                             # 카운트를 올리고
            
        container_i += 1                               # 컨테이너 인덱스를 올림
    
                    
    return count