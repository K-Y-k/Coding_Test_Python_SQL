# 오름차순으로 정렬한다고 했으므로 sort() 함수를 사용

N = int(input())

num_li = []

for _ in range(N):
    num = int(input())

    num_li.append(num)


num_li.sort()                 # 오름차순으로 정렬한다고 했으므로 sort() 함수를 사용

for i in num_li:
    print(i)