import sys

N, M = map(int, input().split())                            # 나무의 수 N,  필요한 나무의 총 높이 M 입력

tree_list = list(map(int, input().split()))                 # 입력한 나무 길이 값들이 저장된 리스트 선언

start = 1                                                   # 나무의 길이의 최소 길이가 1부터이므로 1부터
end = max(tree_list)                                        # 입력한 나무 길이중 제일 큰 값까지 이분탐색의 범위 지정

while start <= end:                                         # 시작 값이 끝의 값보다 작거나 같을 때까지 반복
    mid = (start + end) // 2                                # 중간 값 선언

    cutting_treeLength = 0                                  # 잘린 나무 길이의 총합을 넣을 변수 선언
    for i in tree_list:                                     # 모든 나무를 하나씩 조회해서
        if i >= mid:                                        # 각 나무가 자르려는 길이보다 크면
            cutting_treeLength += i - mid                   # 자르려는 길이 만큼 자를 수 있고 더해준다.
            
    if cutting_treeLength >= M:                             # 잘라진 길이의 총 합이 필요한 길이보다 크거나 같으면 
        start = mid + 1                                     # 우측의 데이터들을 대상으로 다시 탐색하기 위해 시작 값을 중간 값 + 1의 값으로 바꾸기
    else:                                                   # 잘라진 길이의 총 합이 필요한 길이보다 작으면 
        end = mid - 1                                       # 좌측의 데이터들을 대상으로 다시 탐색하기 위해 끝의 값을 중간 값 - 1의 값으로 바꾸기
        
print(end)                                                  # 시작 값이 끝의 값보다 크거나 같아지면 종료되므로 자른 높이의 최대 값인 end 값으로 출력