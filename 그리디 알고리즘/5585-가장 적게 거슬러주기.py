price = int(input())                     # 입력 값
total_price = 1000 - price               # 1000원 - 입력값

return_coin = [500, 100, 50, 10, 5, 1]   # 잔돈 배열로 선언

count = 0                                # 결과 변수 초기화

for i in return_coin :                   # 배열 원소 개수만큼 반복
    count += total_price // i            # 나눈 몫 더하기
    total_price %= i                     # 나머지 가격으로 바꾸기

print(count)