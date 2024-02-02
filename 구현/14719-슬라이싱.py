# 양 옆의 기준으로 가장 큰 값에서 
# 현재 위치에서의 높이를 뺀 값이 현재 위치에서의 물이 고인 양이다.

H, W = map(int, input().split())

block = list(map(int, input().split()))

answer = 0

for i in range(1, W-1):                     # 양 옆을 기준으로하므로 제일 첫값과 끝값을 제외하고 순회
    left_max = max(block[:i])               # 양 옆의 기준으로
    right_max = max(block[i+1:])

    water_area = min(left_max, right_max)   # 양 옆의 기준으로 가장 큰 값에서

    if water_area > block[i]:
        answer += water_area - block[i]     # 현재 위치에서의 높이를 뺀 값이 현재 위치에서의 물이 고인 양이다.

print(answer)