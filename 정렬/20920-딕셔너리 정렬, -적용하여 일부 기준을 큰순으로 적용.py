# 단어가 자주 나오는 빈도도 파악하려면 딕셔너리를 활용해서 담아야 한다.

# 그렇게 담은 딕셔너리의 값을 1.빈도수가 큰기준 2.길이가 긴 기준 3.사전 기준 순으로 적용하려면
# reverse = True가 아니면 기본값이 오름차순이므로 
# -를 붙여 빈도수가 큰순, 길이가 긴 기준으로 적용한다.

import sys

N, M = map(int, sys.stdin.readline().split())

word_dic = {}
answer = 0

for _ in range(N):
    word = str(sys.stdin.readline().rstrip())

    if len(word) >= M:
        if word not in word_dic:
            word_dic[word] = 1
        else:
            word_dic[word] += 1


word_li = list(sorted(word_dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0])))

for w in word_li:
    print(w[0])