N = int(input())

weight = list(map(int, input().split()))  # 입력한 추의 무게들​
weight.sort()                             # 낮은 무게부터 차례로 추를 더해야 구간이 끊기는지 확인이 가능하기에 가장 작은 순으로 정렬

min_weight = 1                            # 첫 기준 값은 문제에서 추 입력할 때 무조건 나와야하는 최소 추의 무게로 설정

for i in weight:                          # 입력한 무게만큼 반복해서
    if min_weight < i:                    # 입력한 무게가 기준 값보다 크면 구간이 겹치지 않는 뜻으로 반복을 빠져나오고
        break
    
    min_weight += i                       # 기준 값보다 작거나 같으면 기준 값에 추의 무게를 더해준다.

print(min_weight)                         # 위 반복에 걸쳐서 나온 기준 값이 결국 구간이 겹치치 않는 값중 최소 값이다.