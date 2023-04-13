N = int(input())                              # 입력 값 선언
Ai = list(map(int,input().split()))           # 입력 값 만큼의 숫자 입력
d = [1]*N                                     # 기본 값이 최소 경우의 수 1이므로 입력 값 만큼의 1로 초기화

# 길이 구하기
for i in range(N):                            # 입력 값 만큼 반복
    for j in range(i):                        # 현재위치 i에서 앞의 위치인 j와 반복 비교
        if Ai[j] < Ai[i] and d[j]+1 > d[i]:   # 만약 현재 위치의 값(Ai[i])이 앞의 위치의 값(Ai[j])보다 크고  
                                              # 현재 위치의 경우의 수d[i]가 앞의 위치의 경우의 수d[j]보다 작은 경우(즉, 앞의 값이 최대값)이면
            d[i] = d[j]+1                     # 앞의 위치의 경우의 수d[j]값(=최대값)에 +1을 한 값으로 적용한다.

print(max(d))                                 # 모든 값이 들어간 d배열 값중 최대 값 출력


# 수열 내용 구하기
max_d = max(d)                                # 가장 큰 경우의 수를 변수로 저장
Ai_list = []

for i in range(N-1, -1, -1):                  # 1씩 감소하는 for문으로 반복
  if d[i] == max_d:                           # d[i]가 가장 큰 경우의 수일 때
    Ai_list.append(Ai[i])                     # Ai_list[]에 추가하고
    max_d -= 1                                # 가장 큰 경우의 수에 1을 빼주어 다음으로 작은 수를 찾게 한다.

Ai_list.reverse()                             # 가장 큰 수부터 저장했기에 반대로 적용한다.
print(*Ai_list)                               # 띄어쓰기 형태로 출력 
                                              # = for i in Ai_list:
                                              #       print(i, end=" ")
