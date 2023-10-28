# 최종 가속도와 현재 가속도를 0으로 초기화한 후
# 입력한 명령 횟수만큼 루프를 돌려
# 가속(1)일 때는 현재 가속도에 가속 값을 더해주고
# 감속(2)일 때는 현재 가속도보다 감속 값이 크면 현재 가속도를 0으로 만들고(마이너스 속도는 없기에)
#               크지 않으면 현재 가속도에 빼주어 적용한다.
# 이렇게 계산한 현재 가속도를 최종 가속도에 최신화 해준다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    answer = 0
    v = 0
    
    for _ in range(N):
        command = list(map(int, input().split()))
        
        if command[0] == 1:
            v += command[1]
        elif command[0] == 2:
            if command[1] > v:
            	v = 0
            else:
                v -= command[1]
        
        answer += v 
            
        
    print('#' + str(test_case), answer)
