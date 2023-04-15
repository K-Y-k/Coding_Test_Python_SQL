# 버블정렬은 N^2의 시간 복잡도를 가진다.
# 문제 조건에 따르면 최대 25 * (10^10)의 시간 복잡도를 가진다.
# 파이썬의 1초당 계산 가능 횟수는 2 * (10^7)이므로, 버블정렬로는 문제를 풀 수 없다.
# 따라서 다른 방식의 정렬을 이용해야 한다.
# 병합정렬을 이용하면 N * log(N)의 시간복잡도가 소요된다. 
# 즉, 5*(10^5) * log(5*(10^5))이므로 시간 복잡도는 해결이 된다.


# 버블정렬 방식
def bubble_sort():
    count = 0
    for i in range(N):                               # 버블정렬은 해당 리스트의 (행 * 열)만큼 반복한다.
        for j in range(1, N):                        # j-1로 비교하므로 index 범위초과 방지하기위해 제일 앞의 원소는 생략 
            if bubble_list[j-1] > bubble_list[j]:    # 앞의 원소가 현재 원소보다 클 경우
                count += 1                           # 교환 카운트를 세고 값을 교환한다.
                temp = bubble_list[j-1]
                bubble_list[j-1] = bubble_list[j]
                bubble_list[j] = temp 
                
    return count

N = int(input())
bubble_list = list(map(int, input().split()))
print(bubble_sort())


# 병합정렬 방식
def merge_sort(start, end):
    global swap_count, bubble_list

    if start < end:                                 # 시작 값이 끝의 값보다 작다면 아직 끝까지 진행된 것이 아니므로 계속 진행
        mid = (start + end) // 2                    # 중간 값 선언
        merge_sort(start, mid)                      # 절반 기준으로 나눈 후의 앞 리스트 기준의 재귀함수 호출
        merge_sort(mid + 1, end)                    # 절반 기준으로 나눈 후의 뒤 리스트 기준의 재귀함수 호출

        a = start                                   # 절반 기준으로 나눈 후의 앞 리스트의 첫번째 위치 값 선언
        b = mid + 1                                 # 절반 기준으로 나눈 후의 뒤 리스트의 첫번째 위치 값 선언
        temp = []                                   # 교체하기 위해 필요한 리스트 선언

        while a <= mid and b <= end:                # 각 절반으로 나눈 앞/뒤 리스트가 모두 끝부분에 위치할 때까지 반복
            if bubble_list[a] <= bubble_list[b]:    # 앞 리스트의 값이 작거나 같으면
                temp.append(bubble_list[a])         # 스왑이 일어날 필요가 없으므로 그대로 앞 리스트 값을 넣고
                a += 1                              # 앞 리스트의 인덱스 증가

            else:                                   # 앞 리스트의 값이 크면
                temp.append(bubble_list[b])         # 교환이 일어나야하므로 뒤 리스트의 값을 넣고
                swap_count += (mid - a + 1)         # 교환 카운트를 증가시키고(남은 앞 리스트의 개수만큼 더해주면 된다.)
                b += 1                              # 뒤 리스트의 인덱스 증가

        if a <= mid:                                # 위 반복을 진행하고도 남은 1번째 리스트의 남은 값들이 있다면
            temp += bubble_list[a:mid + 1]          # 남은 값들 추가
        if b <= end:                                # 위 반복을 진행하고도 남은 1번째 리스트의 남은 값들이 있다면
            temp += bubble_list[b:end + 1]          # 남은 값들 추가

        for i in range(len(temp)):
            bubble_list[start + i] = temp[i]        # 기존 리스트에 지금까지 정렬된 temp 값으로 교체해주어 최신화해준다.

swap_count = 0
N = int(input())
bubble_list = list(map(int, input().split()))
merge_sort(0, N - 1)
print(swap_count)