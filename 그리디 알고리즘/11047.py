n, k = map(int, input().split())    # 동전의 개수와 제시하는 돈 입력
coin_list = list()                  # 동전의 종류를 담기위한 리스트 형태로 초기화
result = 0                          # 결과 변수 초기화

for i in range(n) :                 # n번 만큼 동전 종류 입력하고 리스트 원소에 추가
    coin_list.append(int(input()))

for i in range(n-1, -1, -1) :       # 역순으로 큰 값부터 나누면서 총 결과 반환 
    result += k//coin_list[i]
    k = k % coin_list[i]

print(result)                       # 결과 출력