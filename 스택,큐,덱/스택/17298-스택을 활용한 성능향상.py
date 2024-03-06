# 내가 푼 방식 = 시간 초과
# 매번 N만큼의 for문을 돌면서 모든 원소들에 대해 실시해야 했기에 
# O(N^2)만큼의 시간복잡도가 발생했고 결국 시간초과를 초래했다.

N = int(input())

A = list(map(int, input().split()))
answer = []


for i in range(N):
    for j in range(i, N):
        if A[i] < A[j]:
            answer.append(A[j])
            break
        
        if j == N-1:
            answer.append(-1)
            break

print(' '.join(map(str, answer)))



# 스택 활용 방식
# 스택에는 원소값이 아닌 원소의 인덱스를 넣어주는 목적으로 사용하였다.

# 스택에 최신 인덱스의 값이 현재 비교하는 값보다 크면 넘어가고 다음 인덱스를 스택에 넣어주고 

# 스택에 최신 인덱스의 값이 현재 비교하는 값보다 작으면 오큰수로 
# 정답에 최신 인덱스의 값을 오큰수로 적용하고 최신 인덱스를 지워준다.
# 그리고 남은 최신 인덱스들도 비교하여 오큰수가 되는지 비교한다.

N = int(input())

A = list(map(int, input().split()))
answer = [-1] * N                            # 오큰수가 없을 때의 -1을 미리 초기화
stack = [0]                                  # 제일 첫번째 인덱스 값을 넣은 스택 초기화


for i in range(1, N):                        # 첫번째 원소의 오른쪽 값부터 비교해야하므로 1부터 시작
    while stack and A[stack[-1]] < A[i]:     # 스택이 비어있고 큰수가 나오지 않을 때까지 반복
        # print(i, stack, A[stack[-1]], A[i])
        # 큰 값이 나왔으면
        idx = stack.pop()                    # 스택의 최신 인덱스를 빼와서
        answer[idx] = A[i]                   # 최신 인덱스의 정답 배열에 오큰수 최신화하기
    
    stack.append(i)                          # 다음 오큰수를 구할 인덱스 넣어주기

print(' '.join(map(str, answer)))