# 내가 푼 방식 = 시간복잡도가 O(N^2)라서 메모리 초과로 비효울적
# 직접 for문을 이중으로 돌려 A배열 서로 곱한 값을 B 리스트에 넣어주고
# 오름차순으로 정렬하여
# k번째의 값을 구했다.

N = int(input())
k = int(input())

A = [i for i in range(1, N+1)]
B = []

for i in range(N):
    for j in range(N):
        B.append(A[i] * A[j])

B.sort()

print(B[k])



# 오름차순이 적용되었으므로
# k번째의 값보다 작은 숫자가 몇개인지 찾아내면 k번째의 값이 무슨 숫자인지 알 수 있다.
# 즉, k보다 작은 수의 곱이 몇개인지 찾으면 된다.
# ex) N이 10이라면 10 x 10에서 20보다 작은 수
# 1행 = 1x1 ~ 1x10  = 10개  -> min(20//1, N(=10))
# 2행 = 2x1 ~ 2x10  = 10개  -> min(20//2, N)
# 2행 = 3x1 ~ 3x6   = 6개   -> min(20//3, N)

# mid는 B 리스트를 일렬로 나열했을 때, count번째 값을 나타낸다.
# 즉, A 배열에서 mid보다 작은 값의 개수가 count개인 것이다.

# 1) 어떤 수보다 작은 숫자가 몇개인지 찾아내면 어떤 수가 몇 번째의 숫자인지 알 수 있는 원리를 눈치채기 어렵고
# 2) 이에 따른 카운트 코드와 카운팅 된 값의 크기에 따른 앞 끝 포인터 조정부분도 어렵다.
# 그래서 솔직히 이해하기 너무 어려운 문제다.

N = int(input())
k = int(input())

start = 0
end = k                              # k번째 수는 k보다 클 수 없기 때문에 끝의 인덱스 값을 최댓값으로 정해준다.
answer = 0

while start <= end:
    mid = (start+end) // 2           # mid는 B 리스트를 일렬로 나열했을 때, count번째의 값을 나타낸다.
    count = 0                        # 각 행의

    for i in range(1, N+1):
        count += min(mid//i, N)

    if count >= k:                   # k보다 작은 수의 개수인 count가 k와 같거나 k보다 클 때 해당되는 경우
        answer = mid                 # 정답에 mid 값으로 최신화 해준다.
        end = mid - 1                # 끝의 값을 mid-1로 적용하여 더 작은 값이 되는지 확인한다.
        
    else:                            # k보다 작은 수의 개수인 count가 k보다 작으면
        start = mid + 1              # 앞의 값을 mid+1로 적용하여 count 크기를 늘리도록 만든다.

print(answer)