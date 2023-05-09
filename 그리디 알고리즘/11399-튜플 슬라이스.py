# 이 문제에서 배울 점
# 1) 대기 시간이 가장 작아지는 방법 = 대기시간 작은순으로 정렬
# 2) 각 항위치일 때 첫번째~각항까지 합한 값을 넣기 result +=  sum(atm_list[:i])

n = int(input())                             # 입력할 개수의 n 정수 입력
atm_list = list(map(int, input().split()))   # 리스트 형태로 담기 위한 선언
result = 0                                   # 결과 변수 초기화

atm_list.sort()                              # 기본값으로 오름차순으로 정렬

for i in range(n+1) :                        # for 2중 반복문으로 낮은 순서로 합산
    result += sum(atm_list[:i])              # 처음 값~i번째까지 총 합을 더해간다.

print(result)                                # 결과 출력