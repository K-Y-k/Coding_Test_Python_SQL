# 내가 푼 방식
# 각 부분 길이에 따른 문자들을 추출하는 것이므로
# 부분 길이와 현재 위치를 기준으로 이중 루프를 조회하고 현재 부분 길이에 충족된 부분 문자이면 set에 추가했다.
# set은 자동으로 중복은 제거해주므로 고유의 문자들만 존재하게 된다.

import sys

word = sys.stdin.readline().rstrip()
word_set = set()

for length in range(1, len(word)+1):            # 부분 길이와
    for i in range(len(word)):                  # 현재 위치를 기준으로 이중 루프를 조회하고
        condition_word = word[i:i+length]

        if len(condition_word) == length:       # 현재 부분 길이에 충족된 부분 문자이면
            word_set.add(condition_word)        # set에 추가했다.

print(len(word_set))



# 좀 더 정돈된 코드

import sys

word = sys.stdin.readline().rstrip()
word_set = set()

for i in range(len(word)):                     # 현재 위치
    for length in range(i, len(word)):         # 부분 길이
        word_set.add(word[i:length+1])

print(len(word_set))