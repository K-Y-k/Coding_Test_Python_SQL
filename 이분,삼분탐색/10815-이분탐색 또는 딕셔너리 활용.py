﻿# 이 문제는 일반적인 각 배열을 for 루프를 돌려 if in으로 해당 숫자가 있으면 카운팅하는 방식으로 탐색하면 시간초과가 발생한다. 
# 왜냐하면 입력 값의 범위가 엄청 크기에
# 즉 일반적인 배열 탐색이 아닌 빠른 탐색 방식인 딕셔너리 또는 이분탐색으로 해야한다.

# 이분탐색 방식
N = int(input())                                              # 상근이가 뽑은 N 카드의 개수 입력
Ncard_list = list(map(int, input().split()))                  # 뽑은 카드의 각 숫자를 입력한 카드 리스트
Ncard_list.sort()                                             # 이분탐색을 위해서 오름차순 정렬 

M = int(input())                                              # 상근이가 뽑은 것중 해당 카드가 있는지의 카드 개수 입력
Mcard_list = list(map(int, input().split()))                  # 해당 카드의 각 숫자를 입력한 카드 리스트

result_list = []                                              # 뽑은 카드가 있는지 카운팅한 결과 리스트 선언
for i in Mcard_list:                                          # 비교할 카드에 카운팅하라고 했으므로 비교할 카드로 반복을 돌린다. 
    start = 0                                                 # 비교할 때 각 카드의 인덱스로 비교할 것이기에 인덱스 시작 값 0과
    end = N-1                                                 # 끝의 인덱스 N-1로 선언

    count = 0                                                 # 카운팅할 변수 초기화
    while start <= end:                                       # 시작 값이 끝의 값보다 작거나 같을 때까지 반복
        mid = (start + end) // 2                              # 중간 값 선언

        if Ncard_list[mid] == i:                              # 중간 값 인덱스의 상근이가 뽑은 카드가 비교할 카드가 같다면
            count = 1                                         # 카운팅하고 종료한다. 왜냐하면 중복된 카드는 없다고 했으므로 더 진행할 필요가 없다.
            break 
        elif Ncard_list[mid] < i:                             # 중간 값 인덱스의 상근이가 뽑은 카드가 비교할 카드보다 작다면
            start = mid + 1                                   # 우측의 데이터들을 대상으로 다시 탐색하기 위해 시작 값을 중간 값 + 1의 값으로 바꾸기
        elif Ncard_list[mid] > i:                             # 중간 값 인덱스의 상근이가 뽑은 카드가 비교할 카드보다 크다면
            end = mid - 1                                     # 좌측의 데이터들을 대상으로 다시 탐색하기 위해 끝의 값을 중간 값 - 1의 값으로 바꾸기
         
    result_list.append(count)                                 # 반복문이 끝난 카운팅 값을 결과 리스트에 넣는다.(못찾았으면 0으로 초기화했던 값이 들어갈 것이고 찾았으면 1이 들어갈 것이다.)
    
for i in result_list:                                         # 결과 카운팅 출력
    print(i, end=' ')



# 딕셔너리 방식
N = int(input())
Ncard_list = list(map(int, input().split())) 
M = int(sys.stdin.readline())
Mcard_list = list(map(int, input().split())) 

card_dict = {}                                                # 속도는 딕셔너리를 사용
for i in Ncard_list:
    card_dict[i] = 0                                          # 상근이가 뽑은 카드 리스트를 딕셔너리로 다시 넣는다.

for j in range(M):                          
    count = 0                                                 # 카운트 0으로 초기화
          
    if Mcard_list[j] not in card_dict:                        # 비교할 카드가 뽑은 딕셔너리 카드 리스트에 없으면
        result_list.append(count)                             # 초기화했던 0을 그대로 결과 리스트에 넣기 
    else:                                                     # 딕셔너리 카드 리스트에 있으면
        count = 1                                             # 1을 결과 리스트에 넣기
        result_list.append(count)

for i in result_list:
    print(i, end=' ')