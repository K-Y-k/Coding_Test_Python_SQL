# 현재 건물에서 양쪽 2칸까지 슬라이싱하고 
# 슬라이싱의 최댓 값을 현재 건물 높이에서 빼줄 때 0이면 현재 건물 높이가 제일 높으므로
# 현재 건물을 제외한 양쪽 2칸중 최댓 값을 빼준 값을 정답에 더해준다.

T = 10

for test_case in range(1, T + 1):
    N = int(input())

    answer = 0
    building_li = list(map(int, input().split()))

    for i in range(2, N-2):
        a = building_li[i] - max(building_li[i-2:i+3])                # 슬라이싱의 최댓값을 현재 건물 높이에서 빼줄 때 0이면 현재 건물 높이가 제일 높으므로

        if a == 0:                                                    # 0이면 현재 건물 높이가 제일 높으므로
            high = max(max(building_li[i-2:i], building_li[i+1:i+3])) # 현재 건물을 제외한 양쪽 2칸중
            answer += building_li[i] - high                           # 최대 값을 빼준 값을 정답에 더해준다.

    print('#' + str(test_case), answer)
    