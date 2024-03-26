# 투 포인터를 활용하여
# 두 용액의 합의 0에 가깝게 해야하므로 
# 두 합의 기준 초깃값을 생성하고 
# 각 용액의 두 합의 절댓값이 기준 값보다 작을 경우 0에 가까운 것이므로 기준값을 새로 갱신하고 정답에 넣을 두 용액도 새로 갱신해준다.

# 그 후 두 용액의 합이 음수이면 앞의 값을 1칸 뒤로 전진하고 
#                     양수이면 끝의 값을 1칸 앞으로 전진하여 
# 0에 가깝게 유도하며 비교해나가면 된다.

# 내가 부족했던점
# 두 용액의 합의 결과에 따른 앞 뒤 인덱스 조정 기준을 절댓값을 씌운 합으로 적용했다..
# 절댓값을 씌운 합의 결과는 기준값과의 비교에서만 처리하고 
# 인덱스 조정의 기준은 따로 절댓값을 씌우지 않은 값이어야 음수인지 양수인지를 알고 0에 가깝게 조정할 수 있는 것이다.

N = int(input())

liquid_li = list(map(int, input().split()))
liquid_li.sort()

left = 0
right = N-1

standard = abs(liquid_li[0] + liquid_li[N-1])                       # 두 합의 기준 초깃값을 생성하고 
answer = [(liquid_li[0], liquid_li[N-1])]


while left < right:
    temp = liquid_li[left] + liquid_li[right]

    if abs(temp) < standard:                                        # 각 용액의 두 합의 절댓값이 기준 값보다 작을 경우
        standard = abs(temp)                                        # 0에 가까운 것이므로 기준값을 새로 갱신하고 정답에 넣을 두 용액도 새로 갱신해준다.

        answer.pop()
        answer.append((liquid_li[left], liquid_li[right]))          # 정답에 넣을 두 용액도 새로 갱신해준다.


    if temp < 0:                                                    # 그 후 두 용액의 합이 음수이면 앞의 값을 1칸 뒤로 전진하고 
        left += 1
    else:                                                           #                     양수이면 끝의 값을 1칸 앞으로 전진하여 0에 가깝게 유도하며 비교해나가면 된다.
        right -= 1


print(answer[0][0], answer[0][1])