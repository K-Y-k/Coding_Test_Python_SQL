# 모든 경우의 수를 확인해보아야하므로 for 반복문을 활용한 브루트포스이다.

# 2차원 반복으로 서로 비교하여 몸무게, 키가 모두 큰 경우에만 카운팅을 하고 
#  최종 카운트된 것에 +1을 하면 등수가 된다.

# '구분자'.join()은 문자열인 리스트만 올 수 있다. 다른 형인 경우는 map(str, 리스트)로 형변환을 해주자!


import sys

N = int(input())                                         # 인원 수 입력
people_list = []                                         # 각 사람의 덩치 값을 넣을 리스트
rank_list = []                                           # 각 사람의 등수를 넣을 리스트

for _ in range(N):                                       # 인원수 만큼 반복해서
    kg, tall = map(int, sys.stdin.readline().split())    # 각 사람의 덩치 값을 넣는다.
    people_list.append((kg, tall))
    
    
for i, j in people_list:                                 # 각 사람의 몸무게, 키를 조회
    rank_count = 0                                       # 등수를 매길 카운트 초기화
    
    for k, l in people_list:                             # 비교할 사람을 위한 2차원 반복
        if i < k and j < l:                              # 비교할 사람의 몸무게, 키 모두 작으면
            rank_count += 1                              # 등수를 올린다.
    
    rank_list.append(rank_count + 1)                     # 매겨진 등수 + 1이 그 사람의 등수로 넣는다.
    
print(' '.join(map(str, rank_list)))                     # int형이므로 str으로 변환 후 출력