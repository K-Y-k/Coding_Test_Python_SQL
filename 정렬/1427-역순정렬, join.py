# 숫자의 각 자리수를 역순으로 정렬하기 위해
# 숫자를 문자로 변환시켜 한자리씩 받아서 리스트에 담고
# 담은 리스트를 역순으로 정렬한 후 출력

N = int(input())

num_li = []

for i in str(N):                   # 숫자를 문자로 변환시켜 한자리씩 받아서 리스트에 담고
    num_li.append(int(i))

num_li.sort(reverse=True)          # 담은 리스트를 역순으로 정렬한 후

print(''.join(map(str, num_li)))   # 연속으로 이어붙여서 출력