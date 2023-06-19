# 두 배열을 하나씩 뽑은 후 곱셈을 한 값을 누적하여 
# 누적 값의 최솟값이 되려면 곱셈을 한쪽의 배열에서는 가장 작은수, 다른 한쪽의 배열에서는 가장 큰수를 뽑아 곱해야한다.
# 즉, 각 배열에 한쪽은 오름차순, 한쪽은 내림차순 정렬을 하고난 후 같은 엔덱스에서의 값을 곱하면 된다. 


def solution(A,B):
    answer = 0

    A.sort()                  # 오름차순 정렬
    B.sort(reverse=True)      # 내림차순 정렬
    
    for i in range(len(A)):
        answer += A[i] * B[i] # 최솟값 * 최댓값
    

    return answer