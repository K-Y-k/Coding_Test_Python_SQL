N = int(input())                                     # 입력 개수 선언
card_list = [0] + list(map(int,input().split()))     # 입력한 개수 만큼 각 카드팩 가격 입력
d = [False for _ in range(N+1)]                      # 초기 값을 False로 초기화 0으로 초기화하면 min 함수는 항상 0이 되므로 이용을 못함
 
for i in range(1, N+1):                              # 1부터 입력한 개수 까지 반복
    for j in range(1,i+1):                           # 각 개수일 때마다의 최소 값을 넣는다.
        if d[i] == False :                           # False이면 아직 한번도 비교를 안한 상태이므로 점화식 그대로 넣고
            d[i] = d[i-j]+card_list[j]
        else :                                       # False가 아니면 한번이상은 카드팩의 최소값이 들어가 있으므로 
            d[i] = min(d[i], d[i-j]+card_list[j])    # 비교를 하고 최소 값을 넣는다.

print(d[N])                                          # 모든 반복이 이루어진 최종 최소 값 출력
