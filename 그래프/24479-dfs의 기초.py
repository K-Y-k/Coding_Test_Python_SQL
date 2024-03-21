# dfs에서 각 노드가 최초 몇번째에 방문했는지를 묻는 문제로

# 몇번째 방문했는지를 카운팅할 변수와
# 방문 여부를 카운팅한 변수로 적용하기 위해 각 노드 수 만큼 0으로 초기화 해둔다.

# 입력한 M 만큼 입력한 노드를 서로 연결해주고
# 문제에서 오름차순의 노드번호 순서로 진행한다 했으므로 각 노드에 연결된 노드들을 오름차순으로 정렬처리해준 후

# 입력한 R의 노드부터 방문이 시작하고
# 처음 방문한 노드의 방문 여부를 현재 몇번째인지 카운팅한 변수로 적용하고

# 현재 방문한 노드와 연결된 노드들을 조회하여
# 방문하지 않은 노드만 몇번째인지의 카운팅을 해준 후 해당 노드의 dfs를 진행한다.

# 위 dfs의 모든 작업을 마치면
# 방문여부 배열의 각 인덱스의 값이
# 각 노드번호가 몇번째로 방문했는지의 값이 나온다.

import sys

def dfs(graph, R):
    global visited, count

    visited[R] = count                   # 처음 방문한 노드의 방문 여부를 현재 몇번째인지 카운팅한 변수로 적용하고

    for i in graph[R]:                   # 현재 방문한 노드와 연결된 노드들을 조회하여
        if not visited[i]:               # 방문하지 않은 노드만
            count += 1                   # 몇번째인지의 카운팅을 해준 후
            dfs(graph, i)                # 해당 노드의 dfs를 진행한다.


N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 1

for _ in range(M):                                  # 입력한 M 만큼
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)                              # 입력한 노드를 서로 연결해주고
    graph[b].append(a)

for i in range(N+1):                                # 각 노드에 연결된 노드들을 오름차순으로 정렬처리해준 후
    graph[i].sort()


dfs(graph, R)                                       # 입력한 R의 노드부터 방문이 시작하고

                                                    # 위 dfs의 모든 작업을 마치면
for i in range(1, N+1):                             # 방문여부 배열의 각 인덱스의 값이
    print(visited[i])                               # 각 노드번호가 몇번째로 방문했는지의 값이 나온다.