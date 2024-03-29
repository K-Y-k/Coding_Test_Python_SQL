def GCD(a,b) :                                              # 최대공약수(유클리드 호제) 구하는 함수
    if b == 0 :     
        return a
    else :
        return GCD(b, a%b)


N, S = map(int, input().split())                            # 동생의 명수, 수빈이 위치 입력
Ai_list = list(map(int, input().split()))                   # 동생의 위치 입력

distance_difference_list = []                               # 절댓값(동생 위치 - 수빈 위치)의 리스트 초기화
for i in Ai_list :                                          # 거리 차이를 리스트에 넣어줌
    distance_difference_list.append(abs(i-S))

result = distance_difference_list[0]                        # 차례로 최대공약수를 구하면 공통된 최대공약수가 나오므로
                                                            # 거리 차이의 첫번째 항을 result로 초기화하여 

for i in range(1, N) :                                      # result를 첫번째 최대공약수를 구하는 대상으로 넣고 진행하여 반복해서
    result = GCD(result, distance_difference_list[i])       # 최종 공통된 최대공약수를 구한다.  

print(result)                                               # 결과 출력