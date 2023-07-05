# 내가 푼 방식
# 1. 50보다 작고 홀수이면 2를 곱한 값을 정답에 넣고
# 2. 50보다 작거나 같으면서 짝수이면 2를 나눈 값을 정답에 넣고
# 3. 그외의 경우는 기존 값을 정답에 넣었다.


def solution(arr):
    answer = []
    
    for i in arr:
        if i < 50 and i % 2 == 1:
            temp = i * 2
            answer.append(temp)
        elif i >= 50 and i % 2 == 0:
            temp = i // 2
            answer.append(temp)
        else:
            answer.append(i)
    
    return answer