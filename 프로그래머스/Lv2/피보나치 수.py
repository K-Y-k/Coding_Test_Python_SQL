# 내가 푼 방식 : 재귀 방식 -> 일부 테스트케이스 런타임 에러 발생

def solution(n):
    answer = fibonachi(n)
    return answer

def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonachi(n-1)%1234567 + fibonachi(n-2)%1234567



# 반복문으로 접근한 방식

def solution(n):
    answer = fibonachi(n)
    return answer

