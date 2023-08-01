# 내가 푼 방식
# 각 행렬의 같은 위치의 원소끼리 합하는 것이므로
# 하나의 배열을 기준으로 같은 위치의 다른 배열과 같이 합한 값을 임의의 리스트에 넣고
# 다음 배열 요소로 이동하기 전에 정답 리스트에 합한 값이 들어간 리스트를 넣었다.


def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp_list = []                       # 합한 값들을 넣을 임의의 리스트 초기화
        
        for j in range(len(arr1[i])):        # 하나의 배열을 기준으로 같은 위치의 다른 배열과 같이 합한 값을 임의의 리스트에 넣고
            tmp = arr1[i][j] + arr2[i][j]
            temp_list.append(tmp)
    
        answer.append(temp_list)             # 다음 배열 요소로 이동하기 전에 정답 리스트에 합한 값이 들어간 리스트를 넣었다.
        
    
    return answer