N = int(input())

distance = list(map(int, input().split()))
city_liter = list(map(int, input().split()))

result = 0
liter_standard = city_liter[0]                      # 기준 값을 첫번째 항의 리터 값으로 지정

for i in range(N-1):                                # 리터는 N-1개로 N-1만큼 루프를 돌림
    if city_liter[i] < liter_standard:              # 정한 기준 값을 비교해서 더 작은 리터가 나오면
        liter_standard = city_liter[i]              # 해당  리터로 기준값을 최신화

    result += distance[i] * liter_standard          # 현재 거리 * 최신화된 리터 를 +=로 결과를 쌓기

print(result)