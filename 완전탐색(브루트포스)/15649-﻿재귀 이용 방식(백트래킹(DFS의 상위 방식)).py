# 여기 문제에서 중복되는 값이 안되게 해야하므로 방문처리여부를 해야한다.
# DFS의 향상된 버전인 백트래킹으로 진행되어야한다.
# 백트래킹으로 깊이 끝까지 진행되고 난후 되돌아온 다음 원소에서 깊이 탐색할 때를 위해서 방문여부를 다시 초기화한다


def permutation(index):
    if index == M:
        print(' '.join(map(str, result)))    # join으로 묶어서 한번에 출력
        return
    
    for i in range(1, N+1):                  # 문제에서 1부터 N까지로 index도 동일하게 맞추었다.
        if visited[i]:                       # 방문했었으면
            continue                         # 뛰어넘고
        else:                                # 방문하지 않았으면
            visited[i] = True                # 방문처리를 하고
            result[index] = i                # 결과 값에 넣고
            permutation(index+1)             # 깊이 탐색을 진행하면서
            visited[i] = False               # return된 후 백트랙킹을 하여 다시 False로 지정해서 초기화
    

N, M = map(int, input().split())
visited = [False] * (N+1)                    # 문제에서 1부터 N까지라고 했으므로 index를 동일하게 맞추기위해 N+1
result = [0] * M                             # 결과 값은 숫자 길이인 M만큼 초기화

permutation(0)                               # 최종 결과 값 길이개수만큼의 출력은 M을 기준이므로 result index에 맞춰서 0부터 시작