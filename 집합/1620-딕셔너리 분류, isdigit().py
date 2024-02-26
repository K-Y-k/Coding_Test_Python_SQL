# 내가 푼 방식 - 시간 초과
# 포켓몬 도감이므로 고유한 포켓몬 이름과 그에 따른 도감번호를 부여하므로 딕셔너리를 활용했다.
# 이렇게 포켓몬 이름과 번호를 키와 값 쌍으로 딕셔너리에 저장하고
# 문제에서 이름 또는 번호를 입력하면 매칭되는 번호 또는 이름이 나오므로
# 입력한 값이 숫자이면 for문으로 돌아서 입력한 값과 매칭될 때 키를 찾았다.
# 하지만 이 for문 때문에 시간 초과가 발행했다.

import sys

N, M = map(int, input().split())

pokemon_dic = {}

for i in range(1, N+1):
    name = sys.stdin.readline().strip()

    if name not in pokemon_dic:
        pokemon_dic[name] = i


for _ in range(M):
    x = sys.stdin.readline().strip()

    if x.isdigit():
        for key, val in pokemon_dic.items():
            if val == int(x):
                print(key)
                break
    else:
        print(pokemon_dic[x])



# 번호가 키인 경우도 같이 넣어주면 빠르게 접근 가능하다.

import sys

N, M = map(int, input().split())

pokemon_name_dic = {}
pokemon_idx_dic = {}

for i in range(1, N+1):
    name = sys.stdin.readline().strip()

    if name not in pokemon_dic:
        pokemon_dic[name] = i
        pokemon_idx_dic[i] = name             # 번호가 키인 경우도 같이 넣어주면 빠르게 접근 가능하다.


for _ in range(M):
    x = sys.stdin.readline().strip()

    if x.isdigit():
        print(pokemon_idx_dic[int(x)])
    else:
        print(pokemon_dic[x])