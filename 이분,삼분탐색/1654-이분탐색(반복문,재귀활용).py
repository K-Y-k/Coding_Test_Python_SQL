# 이분탐색의 기초 원리 
# 데이터가 정렬돼 있는 배열에서 특정한 값을 찾아내는 알고리즘이다.

# 동작 원리
# 1. 배열의 중간에 있는 임의의 값을 선택하여 찾고자 하는 값 X와 비교한다. 
# 2. X가 중간 값보다 작으면 중간 값을 기준으로 좌측의 데이터들을 대상으로 다시 탐색하고
#    X가 중간값보다 크면 배열의 우측을 대상으로 다시 탐색한다. 
# 3. 동일한 방법으로 다시 중간의 값을 임의로 선택하고 비교한다. 
# 4. 해당 값을 찾을 때까지 이 과정을 반복한다.

# 이분탐색은 반복문 방식과 재귀 방식 2가지가 있다.

# 반복문 방식
import sys

K, N = map(int, input().split())                                    # 이미 가지고 있는 랜선의 개수 K,  필요한 랜선의 개수 N 입력

K_list = []                                                         # 이미 가지고 있는 랜선 모델링
for _ in range(K):
    Kx = int(sys.stdin.readline().rstrip())
    K_list.append(Kx)

start = 1                                                           # 시작 값과 끝 값 지정
end = max(K_list)                                                

while start <= end:                                                 # 시작 값이 끝 값보다 작거나 같을 때까지 반복
    mid = (start + end) // 2                                        # 중간 값 선언

    count = 0                                                       # 자른 랜선 개수 선언 및 각 K 랜선 길이들에 중간 값을 나누고 더해주어 즉, 자른 랜선 개수가 된다.
    for i in K_list:
        count += i // mid
        
    if count >= N:                                                  # 자른 랜선 개수가 필요한 랜선길이보다 크거나 같으면
        start = mid + 1                                             # 우측의 데이터들을 대상으로 다시 탐색하기 위해 시작 값을 중간 값 + 1의 값으로 바꾸기
    else:                                                           # 자른 랜선 개수가 필요한 랜선길이보다 작으면
        end = mid -1                                                # 좌측의 데이터들을 대상으로 다시 탐색하기 위해 끝의 값을 중간 값 - 1의 값으로 바꾸기
        
print(end)                                                          # 시작 값이 끝의 값보다 크거나 같아지면 종료되므로 최대 길이를 end 값으로 출력
    


# 재귀 방식
import sys

K, N = map(int, input().split())

K_list = []
for _ in range(K):
    Kx = int(sys.stdin.readline().rstrip())
    K_list.append(Kx)

start = 1
end = max(K_list)
    
def binarySearch(start, end, N):
    if start > end:                                                 # 시작 값이 끝의 값보다 크거나 같아지면 종료되므로 최대 길이를 end 값으로 반환
        return end
    
    mid = (start + end) // 2
    
    count = 0
    for i in K_list:
        count += i // mid
        
    if count >= N:
        return binarySearch(mid+1, end, N)
    else:
        return binarySearch(start, mid-1, N)

print(binarySearch(start, end, N))                                 # 위 재귀함수를 거치고 반환된 end 값으로 출력됨
