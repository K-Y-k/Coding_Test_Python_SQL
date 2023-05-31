# 콜라의 빈병의 개수 n이 교환 가능한 최소 숫자 a이상일 때까지 반복
# b개의 병 추가하기
# 남은 병까지 추가로 계산해야한다. (이 부분이 부족)



def solution(a, b, n):
    answer = 0
    
    while True:
        temp = n // a * b          # 전체 n개를 a만큼 나누고 각 개수에 b개의 병만큼 돌려주는 개수
        
        answer += temp             # 위 연산한 개수를 추가

        n = n % a + temp           # 위 연산한 개수뿐만 아니라 나누어 떨어지지 않은 남은 병까지 추가로 넣어줘야 한다!
        
        if n < a:                  # 더 이상 a로 나누어 떨어지지 않을 때 반복 종료
            break
        
    return answer 