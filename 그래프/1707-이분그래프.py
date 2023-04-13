# 이분 그래프는 모든 정점이 기준 정점인 2개의 정점중 하나는 이어져있어 2개의 그룹으로 나눌 수 있는 그래프이다.


import sys

sys.setrecursionlimit(20000)                                   # 재귀호출에 필수
input = sys.stdin.readline


def dfs(start, group):
    global error                                               # error를 전역변수로 가져옴

    if error:                                                  # 만약 사이클이 true라면 재귀탈출
        return

    visited[start] = group                                     # 사이클이 아니면 해당 그룹으로 등록

    for i in edge[start]:                                      # 깊이 탐색을 진행하는데
        if not visited[i]:                                     # 방문하지 않은 정점은
            dfs(i, -group)                                     # -를 붙여서 다른 그룹으로 설정

        elif visited[start] == visited[i]:                     # 인접한데 같은 그룹이라면
            error = True                                       # 에러값 True 
            return                                             # 그후 재귀 리턴


T = int(input())

for _ in range(T):
    V, E = map(int, input().split())                           # 정점, 간선 개수 입력
    
    edge = [[] for _ in range(V+1)]                            # 빈 간선 개수를 인접 리스트로 생성
    visited = [False] * (V+1)                                  # 방문했는지의 여부를 알려주는 리스트 생성
    
    error = False                                              # 이분그래프인지 알고 난 후 dfs를 종료할지의 여부 판단하는 변수로 첫 초기값을 False로 시작

    for _ in range(E):                                         # 간선 입력 값들 등록
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    for i in range(1, V + 1):
        if not visited[i]:                                     # 만약 아직 방문하지 않았다면
            dfs(i, 1)                                          # dfs를 돈다.
            if error:                                          # 만약 에러가 참이라면
                break                                          # 탈출

    if error:
        print('NO')
    else:
        print('YES')