# 내가 시도한 방식 = 방안 틀림
# 행렬 값을 리스트에 넣고
# 각 위치를 차례로 루프를 돌면서 1인 것은 행, 열이 연속으로 1인지 조사하여
# 문제에서 원하는 K 길이와 같으면 카운팅

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    li = []
    answer = 0
    
    for _ in range(N):
        li.append(list(map(int, input().split())))
    
    for i in range(N):
        for j in range(N):
            if li[i][j] == 1:
                row_count = 0
                col_count = 0
                
                for k in range(j, N):
                    if li[i][k] == 1:
                        row_count += 1
                    if li[i][k] == 0 or k == N-1:
                        if row_count == K:
                            answer += 1
                        break
                
                for l in range(i, N):
                    if li[l][j] == 1:
                        col_count += 1
                    if li[l][j] == 0 or l == N-1:
                        if col_count == K:
                            answer += 1
                        break

    print('#' + str(test_case), answer)



# 루프를 돌리는 행에서 행, 렬을 한번에 찾기

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    li = []
    answer = 0
    
    for _ in range(N):
        li.append(list(map(int, input().split())))
    
    for i in range(N):
        row_count = 0
        col_count = 0
        
        # 현재 행에서의 1이 연속된 행 모두 찾기
        for j in range(N):
            if li[i][j] == 1:
                row_count += 1
            if li[i][j] == 0 or j == N-1:
                if row_count == K:
                    answer += 1
                row_count = 0

        # 현재 행에서의 1이 연속된 열 모두 찾기
        for k in range(N):
            if li[k][i] == 1:
                col_count += 1
            if li[k][i] == 0 or k == N-1:
                if col_count == K:
                    answer += 1
                col_count = 0
                
    print('#' + str(test_case), answer)