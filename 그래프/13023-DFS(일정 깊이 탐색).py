# A-B-C-D-E의 관계가 있는지를 확인하는 것이므로 그래프의 깊이가 5만 증명하면 된다.
# 즉. DFS로 조회하여 0부터 시작하기에 깊이가 4이면 A~E가 이어져있다는 것이므로 1을 출력하게 한다. 

import sys

N, M = map(int, input().split())
relation = [[] for i in range(N)]                         # 친구 관계 리스트 선언
visited = [False] * N                                     # 방문했는지의 여부를 판단하기 위해 선언
 
for _ in range(M):                                        # 그래프를 인접 리스트 방식으로 표현
    a, b = map(int, sys.stdin.readline().split())     
    relation[a].append(b)                                 # 입력한 관계를 친구 관계 리스트에 넣어준다.
    relation[b].append(a)                                 # 양방향 그래프이므로 서로 넣어줘야한다.


def dfs(idx, depth):
    if depth == 4:                                        # 깊이가 4이면 1을 출력하고 프로그램 종료
        print(1)
        exit()
    for i in relation[idx]:                               # 재귀호출로 계속 깊이있는 탐색을 진행한다.
        if not visited[i]:
            visited[i] = True                             # dfs의 주의점1: dfs에 들어가기 전 해당 숫자에 대해 방문 체크를 해주고 시작해야한다.
            dfs(i, depth+1)                               # 친구 관계를 확인할 때마다 깊이를 +1 해준다.
            visited[i] = False                            # dfs의 주의점2: 재귀호출을 했다는 것은 백트래킹으로 되돌아갔다는 뜻이므로 현재위치의 방문 여부를 False로 초기화해줘야한다!!
                                                          # dfs에서 빠져나왔다는건 제일 안쪽까지 파고들었다가 다시 나오는 것이기 때문에 방문표시를 풀어줘야함

                                                
for i in range(N):                                        # 노드를 순서대로 방문하며 dfs를 수행
    visited[i] = True                                     # dfs의 주의점1
    dfs(i, 0)                                             # dfs 시작
    visited[i] = False                                    # dfs의 주의점2

print(0)                                                  # 위 dfs의 재귀호출을 모두 진행해도 1출력 및 종료를 못했으면 없는 것이므로 0을 출력