# 이건 외워야하는 부분이라고 생각한다..
# 2차원 행렬 곱셈은 A[n][m] * B[m][k]이다.


def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):                      # 배열1의 전체 길이만큼
        temp = []
        
        for j in range(len(arr2[0])):               # 배열2의 2차원 길이만큼
            a = 0

            for k in range(len(arr1[0])):           # 배열1의 2차원 길이만큼
                a += arr1[i][k] * arr2[k][j]

            temp.append(a)
            
        answer.append(temp)
    
    return answer