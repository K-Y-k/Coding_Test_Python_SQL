# set 집합 방식
# 리스트에 담은 집합 문자들은 set으로 중복을 제거해주고
# 비교할 문자 리스트에서 각 문자를 집합 문자와 비교해서 포함되면 카운팅 해준다.

import sys

N, M = map(int, input().split())

word_set = []
word_li = []
answer = 0

for _ in range(N):
    word_set.append(sys.stdin.readline().strip())

word_set = list(set(word_set))                         # 리스트에 담은 집합 문자들은 set으로 중복을 제거해주고

for _ in range(M):
    word_li.append(sys.stdin.readline().strip())


for i in word_li:                                      # 비교할 문자 리스트에서 각 문자를 집합 문자와 비교해서 포함되면 카운팅 해준다.
    if i in word_set:
        answer += 1

print(answer)



# 딕셔너리 방식
# 집합 문자들은 딕셔너리로 담아서 중복을 제거해주고
# 비교할 문자 리스트에서 각 문자를 집합 문자 딕셔너리와 비교해서 포함되면 카운팅 해준다.
# 속도가 set 집합 방식보다 훨씬 빠름

import sys

N, M = map(int, input().split())

word_dic = {}
word_li = []
answer = 0

for _ in range(N):                                     # 집합 문자들은 딕셔너리로 담아서 중복을 제거해주고
    word_dic[sys.stdin.readline().strip()] = 1

for _ in range(M):
    word_li.append(sys.stdin.readline().strip())


for i in word_li:
    if i in word_dic:
        answer += 1

print(answer)