# 중앙값을 맞추기 위해 정렬처리를 해준 후 평균과 중앙값을 구했다.

num_li = []

for _ in range(5):
    num_li.append(int(input()))

num_li.sort()                       # 중앙값을 맞추기 위해 정렬처리를 해준 후

avg = sum(num_li) // len(num_li)    # 평균과 중앙값을 구했다.
middle_num = num_li[2]

print(avg)
print(middle_num)