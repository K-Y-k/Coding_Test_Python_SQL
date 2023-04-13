n = int(input())                                       # 입력할 개수의 n 정수 입력
atm_list = list(map(int, input().split()))             # 리스트 형태로 담기 위한 선언
result = 0                                             # 결과 변수 초기화

atm_list.sort()                                        # 기본값으로 오름차순으로 정렬

for i in range(1, n+1) :                               # for 2중 반복문으로 낮은 순서로 합산
    for j in range(i) :
        result += atm_list[j]

print(result)                                          # 결과 출력