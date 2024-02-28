# 내가 푼 방식 = 딕셔너리 방식
# 하나의 딕셔너리에 듣지 못한 사람과 보지 못한 사람을 카운팅과 함께 넣어
# 카운팅 값이 2인 것이 듣지도 보지도 못한 사람이므로
# 카운팅 값 기준으로 내림차순한 후
# for문 루프로 조회하여 2인 값을 듣도 보지도 못한 사람 리스트에 넣고 사전순으로 정렬한 후 출력했다.

import sys

N, M = map(int, input().split())


people_dic = {}                               # 하나의 딕셔너리에

for _ in range(N):                            # 듣지 못한 사람과
    name = sys.stdin.readline().strip()

    if name not in people_dic:
        people_dic[name] = 1
    else:
        people_dic[name] += 1

for _ in range(M):                            # 보지 못한 사람을 카운팅과 함께 넣어
    name = sys.stdin.readline().strip()

    if name not in people_dic:
        people_dic[name] = 1
    else:
        people_dic[name] += 1

sort_people_li = sorted(people_dic.items(), key=lambda x:x[1], reverse=True) # 카운팅 값 기준으로 내림차순한 후


no_listen_see_li = []

for name, count in sort_people_li:            # for문 루프로 조회하여
    if count == 2:                            # 2인 값을
        no_listen_see_li.append(name)         # 듣도 보지도 못한 사람 리스트에 넣고

no_listen_see_li.sort()                       # 사전순으로 정렬한 후

print(len(no_listen_see_li))                  # 출력했다.

for i in no_listen_see_li:
    print(i)



# set 방식
# 듣지 못한 사람들과 보지 못한 사람들을 각각 set으로 담고
# 리스트로 둘을 교집합 &로묶으면서 사전순으로 정렬하고 
# 출력했다.

import sys

N, M = map(int, input().split())


no_listen_people = set()                     # 듣지 못한 사람들과

for _ in range(N):
    name = sys.stdin.readline().strip()
    no_listen_people.add(name)


no_see_people = set()                        # 듣지 못한 사람들과 보지 못한 사람들을 각각 set으로 담고

for _ in range(M):
    name = sys.stdin.readline().strip()
    no_see_people.add(name)

no_listen_see_li = sorted(list(no_listen_people & no_see_people)) # 리스트로 둘을 교집합 &로 묶으면서 사전순으로 정렬하고


print(len(no_listen_see_li))

for i in no_listen_see_li:
    print(i)