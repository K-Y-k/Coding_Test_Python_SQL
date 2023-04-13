# 이 문제는 투 포인터로 분할정복 알고리즘 방식을 이용한 Merge Sort로 풀 수 있다.
# 또는 파이썬 특성을 이용한 배열 더하기로 풀 수도 있다.

# 투 포인터로 분할정복 알고리즘 방식을 이용한 Merge Sort 방식
N, M = map(int, input().split())

N_list = list(map(int, input().split()))
M_list = list(map(int, input().split()))

combined = []                                    # 합쳐진 리스트
i = 0                                            # N의 인덱스
j = 0                                            # M의 인덱스

while i < N and j < M:                           # 각각의 포인터 i, j를 이용해 배열의 크기를 비교 후 오름차순으로 정렬해준다.
    if N_list[i] < M_list[j]:
        combined.append(N_list[i])
        i += 1
    else :
        combined.append(M_list[j])
        j += 1
        
if j == M :                                     # 크기를 모두 비교후 남은 배열을 넣어준다.
    combined += N_list[i:]        
elif i == N :
    combined += M_list[j:]
 
print(' '.join(list(map(str, combined))))       # 합쳐진 리스트 출력



# 파이썬의 특성 : 배열 더하기 방식
N, M = map(int, input().split())

N_list = list(map(int, input().split()))
M_list = list(map(int, input().split()))

combined = N_list + M_list                       # 배열 더하기
    
combined.sort()                                  # 오름차순 정렬

print(*combined)                                
# *combined와 동일한 방식 1.print(' '.join(list(map(str, combined)))) 동일한 역할
# *combined와 동일한 방식 2. for i in combined:   
#                                 print(i, end=' ')



# combined = A_list + B_list 대신 다른 방식2
for i in range(N):
    combined.append(N_list[i])
    
for j in range(M):
    combined.append(M_list[j])