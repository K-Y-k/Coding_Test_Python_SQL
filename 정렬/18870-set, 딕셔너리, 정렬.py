# 문제에 의도가 나열한 숫자들을 각 종류의 숫자들 기준으로 몇번째 크기인지의 번호를 매기는 것이므로
# set으로 중복 숫자를 제거해준 리스트를 따로 생성하고 오름차순으로 정렬한 후
# 기존 중복이 포함된 숫자 리스트를 조회하여 중복 제거한 리스트에서의 크기가 몇번째인지 확인해준다.
# 하지만 리스트.index()는 모든 리스트의 내용을 조회하므로 시간초과가 발생한다.

import sys

N = int(input())

x_li = list(map(int, sys.stdin.readline().split()))

x_li_condition = list(set(x_li))                     # set으로 중복 숫자를 제거해준 리스트를 따로 생성하고
x_li_condition.sort()                                # 오름차순으로 정렬한 후

for i in x_li:                                       # 기존 중복이 포함된 숫자 리스트를 조회하여
    print(x_li_condition.index(i), end=' ')          # 중복 제거한 리스트에서의 크기가 몇번째인지 확인해준다.



# 딕셔너리까지 추가한 방식
# 딕셔너리로 접근하면 고유한 키로 빠르게 데이터를 찾을 수 있어 시간 효율이 좋다.

N = int(input())

x_li = list(map(int, sys.stdin.readline().split()))

x_li_condition = list(set(x_li))
x_li_condition.sort()

x_li_dic = {}                                        # 딕셔너리 생성

for i in range(len(x_li_condition)):                 # 딕셔너리 키 값 적용
    x_li_dic[x_li_condition[i]] = i


for i in x_li:                                       # 기존 중복이 포함된 숫자 리스트를 조회하여
    print(x_li_dic[i], end=' ')                      # 딕셔너리로 접근하면 고유한 키로 빠르게 데이터를 찾을 수 있어 시간 효율이 좋다.