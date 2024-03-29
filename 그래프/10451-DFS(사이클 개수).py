import sys
sys.setrecursionlimit(10**6)                              # 최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다


def dfs(idx):                                             # DFS 함수
    visited[idx] = True                                   # 현재 위치의 방문여부를 체크해준다.
    
    for j in graph[idx]:                                  # 현재 위치와 연결된 요소들을 탐색
        if not visited[j]:                                # 아직 방문하지 않은 요소가 있으면 
            dfs(j)                                        # 깊이 탐색 진행
                                                          # 만약 방문하지 않은 요소가 없으면 모두 방문된 상태이므로 재귀가 멈추고 순환하는 그래프라는 것을 암시할 수 있다.

T = int(input())                                          # 테스트 케이스 개수 입력
for _ in range(T):                                        # 테스트 케이스 입력한 개수 만큼 반복
    N = int(sys.stdin.readline().rstrip())                # 순열 개수 입력
    graph = [[] for _ in range(N+1)]                      # 그래프 모델링
    permutation_list = [0] + list(map(int, sys.stdin.readline().rstrip().split()))  # [0]+로 한 이유는 그래프 크기를 N+1만큼 만들었으므로 여기도 N+1만큼 맞춰준 것
    
    for i in range(N+1):                                  # 순차적으로 그래프 모델링 매칭 
        graph[i].append(permutation_list[i])
        
    visited = [False] * (N+1)                             # 방문 여부 False로 초기화
    cycle_count = 0                                       # 사이클 개수 초기화
    
    for i in range(1, N+1):                               # 인덱스 순서대로 탐색 
        if not visited[i]:                                # 만약 방문하지 않았으면
            dfs(i)                                        # 그 위치에서 DFS를 진행하고
            cycle_count += 1                              # 문제에서 순회하지 않는 input은 들어오지 않는 가정이 있으므로 DFS를 완료한 상태면 사이클이 완성된 것이므로 사이클 개수를 +1 해줌
            
    print(cycle_count)



#- 개선점 : 나는 그래프 모델링을 기본적으로 하는 것이 습관이 되어 저렇게 했지만 모델링 따로 없이 진행할 수 있다.
import sys
sys.setrecursionlimit(10**6)


def dfs(idx):
    visited[idx] = True
    next_idx = permutation_list[idx]        # 다음 요소를 저장
    
    if not visited[next_idx]:               # 다음 요소가 방문된 상태가 아니면
        dfs(next_idx)                       # 재귀 호출로 방문


T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    
    permutation_list = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    
    visited = [False] * (N+1)
    cycle_count = 0
    
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cycle_count += 1
            
    print(cycle_count)