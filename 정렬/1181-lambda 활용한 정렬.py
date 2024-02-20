# 문제에서 정렬 기준을 길이가 짧은 순으로 하고 길이가 같은 경우는 단어 철자순이므로
# 중복도 제거해달라고 했으므로 set으로 중복처리를 한 후
# 먼저 단어 철자기준으로 오름차순으로 한 후
# 길이순으로 오름차순을 하고 출력했다.

import sys

N = int(input())

word_li = []

for _ in range(N):
    word_li.append(sys.stdin.readline().strip())        # sys.stdin.readline()은 \w 개행문자까지 가져오므로 strip()으로 개행문자를 제거해줘야한다!
                                                        # input()은 개행문자를 제거해줌
    
word_li = list(set(word_li))                            # 중복도 제거해달라고 했으므로 set으로 중복처리를 한 후

word_li.sort()                                          # 먼저 단어 철자기준으로 오름차순으로 한 후
word_li = sorted(word_li, key=lambda x:(len(x)))        # 길이순으로 오름차순을 적용한다.
# word_li = sorted(word_li, key=len)
# word_li.sort(key=len)

for i in word_li:
    print(i)