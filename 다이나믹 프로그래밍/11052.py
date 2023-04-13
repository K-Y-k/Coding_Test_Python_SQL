N = int(input())                                    # 입력 개수 선언

card_price = [0] + list(map(int,input().split()))   # 입력한 개수 만큼 각 카드팩 가격 입력
d = [0]*(N+1)                                       # 입력한 개수 만큼의 배열 초기화

for i in range(1, N+1):                             # 1부터 입력한 개수 까지 반복
    for j in range(1, i+1):                         # 각 개수일 때마다의 최대 값을 넣는다.
        d[i] = max(d[i], d[i-j]+card_price[j])      # 점화식

print(d[N])                                         # 최대 값 출력


# 점화식 부연 설명
# 최대로 구하라고 해서 max이고 
# 마지막이 오는 카드팩의 카드 개수가 몇개짜리인지 모르기에 i개를 샀다.  => p[i](위 코드에서는 card_price[j])
# 즉, p[i]로 정의할 수 있고 그렇게되면 나머지는 d[n-i]인 것이다.
# 시간 복잡도 = 각 카드를 구매하는 개수인 N개 x 하나의 칸을 구하는데 걸리는 시간 i = O(N^2)