# 주요 포인트
# 1) 이동하는 moves가 행의 기준이고 board의 열 부분이 각 인형을 뽑는 라인
# 2) 스택이 이전 값이 있는지의 여부는 len(stack) > 1
# 3) 뽑은 작업이 끝나면 break으로 다음 열 조회를 그만두고 다음 moves를 조회해야함


def solution(board, moves):
    answer = 0
    stack = []
    
    for i in moves:                             # 이동한 것을 행의 기준으로 
        for j in range(len(board)):             # 행렬 판에 열을 조회할 때
            if board[j][i-1] != 0:              # 0이 아니면 인형이 있는 것이므로
                stack.append(board[j][i-1])     # 스택에 현재 값을 넣고
                board[j][i-1] = 0               # 0으로 비워준다.
                
                if len(stack) > 1:              # 스택이 현재 이전 값과 비교할 수 있는 상황이면
                    if stack[-1] == stack[-2]:  # 이전 값과 현재 넣은 값과 비교하여 같으면
                        answer += 2             # 같은 종류의 인형이므로 답에 적용해주고
                        stack.pop()             # 이전과 현재 값들을 지워준다.
                        stack.pop()
                        
                break                           # 현재 꺼낸 작업이 완료된 것이므로 중단하고 다음 moves를 불러와야한다. 
                
    return answer