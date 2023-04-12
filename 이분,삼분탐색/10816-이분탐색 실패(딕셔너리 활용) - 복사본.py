# 이 문제는 이분탐색으로 접근하면 시간초과가 발생한다. 결국 딕셔너리를 활용해야했다.

# 내가 푼 이분탐색 방식
N = int(input())
Ncard_list = list(map(int, input().split()))
Ncard_list.sort()

M = int(input())
Mcard_list = list(map(int, input().split()))

result_list = []

for i in Mcard_list:
    
    start = 0
    end = N-1
    
    while start <= end:
        mid = (start + end) // 2
        
        count = 0
        if Ncard_list[mid] == i:
            count = Ncard_list.count(i)
            break
        elif Ncard_list[mid] > i:
            end = mid -1
        elif Ncard_list[mid] < i:
            start = mid + 1
    result_list.append(count)
        
for i in result_list:
    print(i, end=' ')


# 딕셔너리 활용 방식
N = int(input())
Ncard_list = list(map(int, input().split()))         # 상근이가 뽑은 카드 숫자 리스트

N_dic = {}                                             # 딕셔너리 선언
for i in Ncard_list:                                   # 딕셔너리에 상근이가 뽑은 카드의 각 개수를 넣기
    if i in N_dic:
        N_dic[i] += 1
    else:
        N_dic[i] = 1
        
M = int(input())
Mcard_list = list(map(int, input().split()))        # 비교할 카드 숫자 리스트 

for i in Mcard_list:                                   # 비교할 각 카드들로 
    if i in N_dic:                                       # 상근이가 뽑은 카드와 같은 숫자이면
        print(N_dic[i], end=' ')                       # 같은 숫자의 개수를 출력
    else:                                                 # 상근이가 뽑은 숫자가 없으면
        print(0, end=' ')                               # 0개이므로 0출력


#﻿ collections 모듈의 Counter 클래스 활용 방식
# 각 원소의 개수를 딕셔너리 형태로 반환시켜 주는 Counter 클래스이다.
from collections import Counter                       # collections의 Counter 클래스 선언

N = int(input())
Ncard_list = list(map(int, input().split()))

M = int(input())
Mcard_list = list(map(int, input().split()))

count = Counter(Ncard_list)                             # 상근이가 뽑은 카드 리스트가 들어간 Counter 클래스를 적용한 카운트 리스트 선언
                                                               # 예시로 Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1}) 이런식으로 저장되어 있을 것이다.

for i in Mcard_list:
    print(count[i], end=' ')                               # 비교할 카드와 같은 상근이가 뽑은 카드의 개수 출력