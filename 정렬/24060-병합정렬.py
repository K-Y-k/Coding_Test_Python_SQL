# 병합 정렬 알고리즘인데
# 문제에서는 K번째로 저장되는 숫자를 원하므로
# merge 함수 실행 과정중 결과를 저장하는 부분에서 횟수를 세어주는 변수를 추가하여 활용한다.

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)            # A[p..q]을 오름차순으로 정렬
        merge_sort(A, q + 1, r)        # A[q+1..r]을 오름차순으로 정렬
        merge(A, p, q, r)


def merge(A, p, q, r):                 # A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
    global count, answer

    tmp = []
    i = p
    j = q + 1

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:                      # 왼쪽 배열 부분이 남은 경우
        tmp.append(A[i])
        i += 1

    while j <= r:                      # 오른쪽 배열 부분이 남은 경우
        tmp.append(A[j])
        j += 1

    i = p
    t = 0

    while i <= r:                      # 결과를 A[p..r]에 복사
        A[i] = tmp[t]

        count += 1                     # merge 함수 실행 과정중 결과를 저장하는 부분에서 횟수를 세어주어
        if count == K:                 # K번째까지 카운팅되면 
            answer = A[i]              # 문제에서 원하는 값이므로 저장하고 종료
            break

        i += 1
        t += 1


N, K = map(int, input().split())

num_li = list(map(int, input().split()))
count = 0
answer = -1                           # K번째 이전에 병합정렬이 끝날 수 있으므로 -1로 초기화

merge_sort(num_li, 0, N-1)

print(answer)