# 리스트로 정렬한 방식 - 시간초과
# enter이면 리스트에 넣고
# leave이면 리스트에서 해당 사람이름을 제거해준다.
# 현재 enter중인 리스트에서 사전명 내림차순이라고 했으므로 정렬 처리해준 후 출력한다.

import sys

N = int(input())
enter_li = []

for _ in range(N):
    name, process = map(str, sys.stdin.readline().strip().split())

    if process == 'enter':
        enter_li.append(name)
    else:
        enter_li.remove(name)


enter_li.sort(reverse=True)

for i in enter_li:
    print(i)



# 딕셔너리 방식 
# 딕셔너리에서의 정렬은 sorted만 가능하고 이 sorted 함수는 정렬된 리스트로 변환해서 넣어준다.

import sys

N = int(input())
enter_dic = {}

for _ in range(N):
    name, process = map(str, sys.stdin.readline().strip().split())

    if process == "enter":
        enter_dic[name] = process
    else:
        del enter_dic[name]                                                      # 딕셔너리에서 삭제 방법


# 딕셔너리에서의 정렬은 sorted만 가능하고 이 함수는 정렬된 리스트로 변환해서 넣어준다.
enter_dic = sorted(enter_dic.keys(), reverse=True)                               # 여기서는 keys()아므로 키만 넣은 정렬된 리스트를 반환한다.
# enter_dic = sorted(enter_dic.items(), key=lambda x:x[0], reverse=True)         # 여기서는 키, 값 모두 들어간 정렬된 리스트를 반환한다.

for key in enter_dic:
    print(key)