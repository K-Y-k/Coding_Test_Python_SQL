# 중앙 값이랑 범위는 쉽고 첫째자리 반올림이랑 최빈 값에서 애먹었다.
# 첫째 자리라고 하길래 따로 함수가 있을 줄 알았지만 round()함수를 사용하면 됐다..

# 최빈 값은 여러 개가 나오므로 딕셔너리에 각 카운팅하고 딕셔너리를 조회하여 최대 빈도수이면 
# 최대 빈도수 리스트에 새로 넣어 여러 개가 들어 있으면 정렬하여 2번째의 수를 적용하였다.

# 참고로 sys.stdin.readline()으로 입력하지 않으면 시간초과가 발생한다.
# 숫자 범위가 -4000~4000로 총 8000까지 올 수 있어 반복 범위가 넓어서 그런 것 같다.



import sys

N = int(input())                             # 수가 들어있는 개수 입력
num_list = []                                # 수를 넣을 리스트 선언

for _ in range(N):                           # 개수 만큼 수를 입력하여 넣는다.
    num = int(sys.stdin.readline())
    num_list.append(num)
    
operation1 = round(sum(num_list) / N)        # 수의 총합 / 개수에 첫째소수까지 반올림한 산술평균 연산 


num_list_sorted = sorted(num_list)           # 중앙 값을 구하기 위한 정렬 sorted는 단독으로 온다. 리스트변수.sort()와 햇갈리지 말기
operation2 = num_list_sorted[N//2]           # 0부터 시작하므로 2를 나눈 몫이 결국 중앙 값이 된다. 


frequency = dict()                           # 빈도수를 저장할 딕셔너리 선언
for i in num_list:                           # 수를 조회하고
    if i in frequency:                       # 빈도수 딕셔너리에 저장되어있는 상태면
        frequency[i] += 1                    # +1 해주고
    else:                                    # 없으면
        frequency[i] = 1                     # 1로 새로 넣어준다.
        
max_frequency = max(frequency.values())      # 딕셔너리변수.values()로 최대 빈도수를 가져오고
max_frequency_list = []                      # 최대 빈도수가 여러 개가 올 수 있다고 하여 최대 빈도수만 넣어줄 리스트 선언

for i in frequency:                          # 빈도수 딕셔너리를 조회하여
    if frequency[i] == max_frequency:        # 최대 빈도수인 숫자면
        max_frequency_list.append(i)         # 최대 빈도수 리스트에 넣어준다.
        
if len(max_frequency_list) > 1:              # 최대 빈도수 리스트가 2개이상이면 여러 개이므로
    max_frequency_list.sort()                # 정렬하고
    operation3 = max_frequency_list[1]       # 2번째 수를 가져온다.
else:                                        # 1개이면
    operation3 = max_frequency_list[0]       # 첫 항을 가져온다.

    
operation4 = max(num_list) - min(num_list)   # 범위 연산은 최대-최소 값이라고 했으므로 적용


print(operation1)                            # 위 연산을 최종 출력
print(operation2)
print(operation3)
print(operation4)