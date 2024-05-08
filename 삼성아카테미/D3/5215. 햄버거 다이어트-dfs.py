# 각 재료를 1.추가한다 2.추가하지 않는다의 경우의 수로 dfs 탐색하면 모든 경우의 수들이 진행되는데
# 이때 기준 칼로리까지 해당하는지와 끝까지 진행했는지에 대한 가지치기를 한다.

# 이 진행 중에 현재 추가한 재료의 맛이 최대 값인지에 대한 갱신을 진행해주면 
# 기준에 해당하는 모든 경우가 진행되면서 최대 맛을 확인할 수 있다.


def dfs(idx, taste, kcal):
    global max_taste

    if kcal > L:             # 기준 칼로리까지 해당하는지에 대한 기지치기
        return
    
    if idx == N:             # 끝까지 진행했는지에 대한 가지치기
        return
    
    if taste > max_taste:    # 이 진행 중에 현재 추가한 재료의 맛이 최대 값인지에 대한 갱신을 진행
        max_taste = taste

    dfs(idx+1, taste + ingredient_li[idx][0], kcal + ingredient_li[idx][1]) # 현재 재료를 1.추가한다
    dfs(idx+1, taste, kcal)                                                 # 2.추가하지 않는다의 경우의 수로 dfs 탐색


T = int(input())

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    max_taste = 0

    ingredient_li = []
    for _ in range(N):
        ingredient_li.append(list(map(int, input().split())))

    dfs(0, 0, max_taste)
    
    print('#'+str(test_case), max_taste)