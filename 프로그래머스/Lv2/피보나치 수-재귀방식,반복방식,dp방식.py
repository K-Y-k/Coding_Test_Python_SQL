# 내가 푼 방식 : 재귀 방식 -> 일부 테스트케이스 런타임 에러 발생
# 재귀적인 방법이 사람이 보기에 더 직관적이나 훨씬 오래걸리고 비효율적이라고 한다.

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
    


# 반복 방식

def solution(n):
    fiboachi = [0, 1]                                   # F(0), F(1)일 때 초깃값 지정

    for i in range(2, n+1):
        fiboachi.append(fiboachi[i-1] + fiboachi[i-2])  # 연산된 값을 리스트안에 넣기
    
    answer = fiboachi[-1] % 1234567                     # 제일 마지막 항목이 구하고 싶은 값
    
    return answer



# dp 방식

def solution(n):
    fiboachi = [0] * 100001                             # 문제에서 100000까지라고 했으므로 최대 공간까지 미리 설정 및 초기화
    fiboachi[0] = 0                                     # F(0)일 때 초깃값 지정
    fiboachi[1] = 1                                     # F(1)일 때 초깃값 지정

    for i in range(2, n+1):                             # F(2)부터 F(n)까지 점화식 적용
        fiboachi[i] = fiboachi[i-1] + fiboachi[i-2]
    
    answer = fiboachi[n] % 1234567
    
    return answer


    


