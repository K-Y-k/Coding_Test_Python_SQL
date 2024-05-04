# 덤프 횟수만큼 제일 높은 곳의 상자를 제일 낮은 곳으로 옮기므로
# 덤프 횟수만큼 제일 높은 값을 -1 해주고 제일 낮은 값을 +1 해주면 된다.

T = 10

for test_case in range(1, T + 1):
    dump = int(input())

    wall_li = list(map(int, input().split()))

    for i in range(dump):                          # 덤프 횟수만큼
        wall_li[wall_li.index(max(wall_li))] -= 1  # 제일 높은 값을 -1 해주고 
        wall_li[wall_li.index(min(wall_li))] += 1  # 제일 낮은 값을 +1 해주면 된다.

    answer = max(wall_li) - min(wall_li)
    print('#' + str(test_case), answer)