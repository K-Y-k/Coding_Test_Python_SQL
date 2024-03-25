# 내가 푼 방식 combination 활용 = 시간초과
# 2개의 한쌍의 모든 경우의 수를 combination으로 구한 후 두 수의 합이 X인 경우 정답에 카운팅 해줬다.
# O(C(n, k) * k)이기에 문제에서의 데이터 범위가 커서 시간초과가 발생한다.

from itertools import combinations

N = int(input())
num_li =list(map(int, input().split()))
x = int(input())

c = combinations(num_li, 2)
answer = 0


for i in c:
    if i[0] + i[1] == x:
        answer += 1


print(answer)



# 투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘을 의미한다
# 좌, 우 방향의 인덱스를 이용하여 한 번의 배열 탐색으로 두 수의 합이 x가 되는 쌍을 찾을 수 있다.

# 두 수의 합의 결과에 따라 좌, 우의 인덱스를 조절하기 위해서는 정렬(오름차순)을 해주어야 한다.
# 투 포인터 탐색은 왼쪽, 오른쪽 방향의 인덱스가 서로 만날 때(교차할 때)까지 진행하면 된다.

# 정렬 후 3가지 경우에 따라 투 포인터 탐색을 진행하면 된다.
# 1.두 수의 합이 x인 경우는 정답에 카운팅해주고 더 있을 수 있으므로 앞의 값을 한칸 올린다.
# 2.두 수의 합이 x보다 작은 경우는 더 큰 값을 더해야 하므로 앞의 값을 한칸 올린다.
# 3.두 수의 합이 x보다 큰 경우는 더 작은 값을 더해야 하므로 끝의 값을 한칸 낮춘다.

N = int(input())
num_li =list(map(int, input().split()))
x = int(input())

answer = 0
left = 0                                         # 좌 인덱스 초기화
right = N-1                                      # 우 인덱스 초기화

num_li.sort()                                    # 두 수의 합의 결과에 따라 좌,우의 인덱스를 조절하기 위해서는 정렬(오름차순)을 해주어야 한다


while left < right:                              # <=이 안되는 이유는 문제에서는 항상 서로 다른 2개의 한쌍으로 비교해야 하기에
    if num_li[left] + num_li[right] == x:        # 1.두 수의 합이 x인 경우는 정답에 카운팅해주고 더 있을 수 있으므로 앞(좌)의 값을 한칸 올린다.
        left += 1
        answer += 1
    elif num_li[left] + num_li[right] < x:       # 2.두 수의 합이 x보다 작은 경우는 더 큰 값을 더해야 하므로 앞(좌)의 값을 한칸 올린다.
        left += 1
    else:                                        # 3.두 수의 합이 x보다 큰 경우는 더 작은 값을 더해야 하므로 끝(우)의 값을 한칸 낮춘다.
        right -= 1


print(answer)