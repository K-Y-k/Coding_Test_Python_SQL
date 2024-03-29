# 이분탐색은 
# 정렬된 배열을
# 배열의 중간 값을 선택하고 찾고자 하는 값과 비교하여 탐색 범위를 반으로 줄여가는 방식으로 동작한다.

# 이분 탐색은 정렬된 배열에서만 사용 가능하다.
# 시간 복잡도는 O(log n)이다.

N = int(input())
A = list(map(int, input().split()))

M = int(input())
suggest_num = list(map(int, input().split()))

A.sort()

for i in suggest_num:
    start = 0
    end = N-1
    isFind = False

    while start <= end:
        mid = (start + end) // 2

        if i == A[mid]:
            isFind = True
            print(1)
            break
        elif i > A[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if not isFind:
        print(0)



# set을 활용한 방식
# set으로 중복되는 값을 제외해주어 반복되는 횟수를 줄였기에 시간초과가 발생하지 않았다.
        
N = int(input())
A = set(map(int, input().split()))

M = int(input())
suggest_num = list(map(int, input().split()))

for i in suggest_num:
    if i in A:
        print(1)
    else:
        print(0)