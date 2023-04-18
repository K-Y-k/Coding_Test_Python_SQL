import sys

N = int(input())

candy_list = []
for i in range(N):                                                                       # 사탕 리스트 모델링
    candy_x = list(sys.stdin.readline().rstrip())
    candy_list.append(candy_x)

    
def checkCount(candy_list):                                                              # 연속되는 개수 확인 함수
    temp_count = 1                                                                       # 연속되는 개수중 제일 큰 값을 넣을 변수
    
    for i in range(N):                                                                   # 모든 행,열을 조회
        count = 1                                                                        # 기본 연속되는 같은 값은 1개는 있기에 1로 초기값 지정
        for j in range(1, N):                                                            # 행에 대한 부분 조회
            if candy_list[i][j]  == candy_list[i][j-1]:                                  # 같은 행에서의 앞/뒤 행의 값이 같으면 
                count += 1                                                               # 같은 사탕이므로 개수 증가
            else:
                count = 1                                                                # 다르면 새로운 연속이 시작되므로 1개로 다시 지정한다.
                
            if temp_count < count:                                                       # 위 카운팅한 연속 개수 값이 연속되는 개수중 제일 큰 값을 넣는 변수 값보다 크면
                temp_count = count                                                       # 최신화해준다.
                
        count = 1                                                                        # 기본 연속되는 같은 값은 1개는 있기에 1로 초기값 지정
        for j in range(1, N):                                                            # 열에 대한 부분 조회
            if candy_list[j][i]  == candy_list[j-1][i]:                                  # 같은 열에서의 앞/뒤 열의 값이 같으면
                count += 1                                                               # 같은 사탕이므로 개수 증가
            else:
                count = 1                                                                # 다르면 새로운 연속이 시작되므로 1개로 다시 지정한다.
                
            if temp_count < count:                                                       # 위 카운팅한 연속 개수 값이 연속되는 개수중 제일 큰 값을 넣는 변수 값보다 크면
                temp_count = count                                                       # 최신화해준다.
    
    return temp_count                                                                    # 모든 루프를 돌고 난 최종 최대 연속개수를 반환한다.
    
    
result = 0                                                                               # 최종 값 선언
for i in range(N):                                                                       # 모든 행렬에서 확인
    for j in range(N):
        # 열의 오른쪽과 비교
        if j+1 < N:                                                                      # 열이 인덱스 범위에 벗어나지 않으면
            candy_list[i][j], candy_list[i][j+1] = candy_list[i][j+1], candy_list[i][j]  # 현재 위치와 오른쪽 위치의 값을 교환하고
            
            temp_count = checkCount(candy_list)                                          # 교환된 상태에서 연속 개수를 가져와서
            if temp_count > result:                                                      # 제일 큰 값으로 최종 값에 반영하고
                result = temp_count
            
            candy_list[i][j], candy_list[i][j+1] = candy_list[i][j+1], candy_list[i][j]  # 다시 원래의 위치로 되돌려준다.
            
        # 행의 아래쪽과 비교    
        if i+1 < N:                                                                      # 행이 인덱스 범위에 벗어나지 않으면
            candy_list[i][j], candy_list[i+1][j] = candy_list[i+1][j], candy_list[i][j]  # 현재 위치와 오른쪽 위치의 값을 교환하고
            
            temp_count = checkCount(candy_list)                                          # 교환된 상태에서 연속 개수를 가져와서
            if temp_count > result:                                                      # 제일 큰 값으로 최종 값에 반영하고
                result = temp_count
            
            candy_list[i][j], candy_list[i+1][j] = candy_list[i+1][j], candy_list[i][j]  # 다시 원래의 위치로 되돌려준다.
            
print(result)