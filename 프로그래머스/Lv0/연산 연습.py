# 합
def solution(num1, num2):
    answer = num1 + num2
    return answer

# 차
def solution(num1, num2):
    answer = num1 - num2
    return answer

# 곱셈
def solution(num1, num2):
    answer = num1 * num2
    return answer

# 나눗셈
def solution(num1, num2):
    answer = int(num1 / num2)
    return answer

# 몫
def solution(num1, num2):
    answer = num1 // num2
    return answer

# 나머지
def solution(num1, num2):
    answer = num1 % num2
    return answer


# 비교
def solution(num1, num2):
    answer = 0
    
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    
    return answer