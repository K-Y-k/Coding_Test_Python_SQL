# 내가 푼 방식
# 하나의 방향에서 하나의 길이만 있으면 최대 길이로 간주하여 이 길이들로 큰 사각형의 넓이를 구했고 
# 하나의 방향에서 두 길이가 있으면 이 두 길이중 최소값으로 작은 사각형으로 간주하여 넓이를 구했다.
# 하지만 여기서 모순은 항상 작은 값이 빈 공간의 사각형이 아니라는 것이다.

K = int(input())

graph = [[] for _ in range(5)]

for _ in range(6):
    direction, distance = map(int, input().split())

    graph[direction].append(distance)

graph.remove(graph[0])

max_distance = []
min_distance = []

for i in graph:
    if len(i) > 1:                             # 하나의 방향에서 하나의 길이만 있으면 
        min_distance.append(min(i[0], i[1]))   # 최대 길이로 간주하여 이 길이들로 가장 큰 사각형의 넓이를 구했고
        
    else:                                      # 하나의 방향에서 두 길이가 있으면 
        max_distance.append(i[0])              # 이 두 길이중 최소값으로 작은 사각형으로 간주하여 넓이를 구했다.

max_area = max_distance[0] * max_distance[1]   # 가장 큰 사각형의 넓이를 구했고
min_area = min_distance[0] * min_distance[1]   # 작은 사각형으로 간주하여 넓이를 구했다. 

answer = (max_area - min_area) * K

print(answer)



# 6변의 방향으로 인덱스 접근하여 계산
# 6변으로 기준을 두고 루프를 돌아 현재 변과 다음 마주하는 변의 곱으로 최대 사각형의 넓이를 계산하고
# 이때 최대 사각형일 경우 현재 변의 인덱스를 저장하고
# 저장했던 인덱스에서 3칸 이동한 변과 4칸 이동한 변의 곱이 항상 빈 공간의 사각형의 넓이가 되어 이 사각형의 넓이를 빼주면 된다! 

K = int(input())

graph = []

for _ in range(6):
    direction, distance = map(int, input().split())

    graph.append(distance)

max_area = 0
small_area = 0
standard_idx = 0

for i in range(6):                             # 6변으로 기준을 두고 루프를 돌아
    temp_area = graph[i] * graph[(i+1) % 6]    # 현재 변과 다음 마주하는 변의 곱으로 최대 사각형의 넓이를 계산하고

    if max_area < temp_area:                   # 이때 최대 사각형일 경우 현재 변의 인덱스로 기준 인덱스를 갱신하고
        max_area = temp_area
        standard_idx = i

small_area = graph[(standard_idx+3) % 6] * graph[(standard_idx+4) % 6] # 저장했던 인덱스에서 3칸 이동한 변과 4칸 이동한 변의 곱이 항상 빈 공간의 사각형의 넓이가 되어 이 사각형의 넓이를 빼주면 된다! 


answer = (max_area - small_area) * K

print(answer)