T = int(input())                                                      # 테스트 횟수 입력
for _ in range(T):                                                    # 테스트 입력 횟수만큼 반복
    n = int(input())                                                  # 열 길이 입력
    
    sticker_n1 = [0] + list(map(int,input().split()))                 # 1행의 스티커 값 입력
    sticker_n2 = [0] + list(map(int,input().split()))                 # 2행의 스티커 값 입력
    sticker_value = list(zip(sticker_n1,sticker_n2))                  # 1행, 2행 하나의 리스트로 합침(zip 함수는 각 동일한 위치의 값을 합친다.)
    
    d = [[0]*3 for _ in range(n+1)]                                   # 뜯지 않음, 위 뜯기, 아래 뜯기 3가지로 초기화
    
    for i in range(1, n+1):                                           # 열 길이 만큼 반복
        d[i][0] = max(d[i-1])                                         # 뜯지 않았을 때는 앞의 번째는 모든 상황이 가능하므로 모든 값 중 최대 값
        
        d[i][1] = max(d[i-1][0],d[i-1][2]) + sticker_value[i][0]      # 위쪽을 뜯었을 때
        # 뜯지 않음 + 아래쪽 스티커 뜯음의 각 모든 경우의 수 중 최대값 + 현재 위치의 위쪽에 뜯은 스티커 값
        
        d[i][2] = max(d[i-1][0],d[i-1][1]) + sticker_value[i][1]      # 아래쪽을 뜯었을 때
        # 뜯지 않음 + 위쪽 스티커 뜯음의 각 모든 경우의 수 중 최대값 + 현재 위치의 아래쪽에서 뜯은 스티커 값

    print(max(d[n]))                                                  # 입력한 길이에서의 최대 값 출력

