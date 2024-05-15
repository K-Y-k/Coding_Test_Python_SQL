# 결국 첫항의 변의 길이가 2개가 있으면 나머지 한개의 변의 길이가 답이고
# 나머지 경우인 첫항의 변의 길이가 1개이거나 3개이면 첫항의 변의 길이가 답이다.

sideLength_li = list(map(int, input().split()))
answer = 0

if sideLength_li.count(sideLength_li[0]) == 2: # 첫항의 변의 길이가 2개가 있으면 
    for i in sideLength_li:                    # 나머지 한개의 변의 길이가 답이고
        if i != sideLength_li[0]:
            answer = i
else:                                          # 나머지 경우인 첫항의 변의 길이가 1개이거나 3개이면
    answer = sideLength_li[0]                  # 첫항의 변의 길이가 답이다.

print(answer)
    