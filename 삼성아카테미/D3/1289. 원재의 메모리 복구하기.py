# 문제에서 주어진 메모리 상태와 모두 0으로 초기화된 현재 메모리를 선언한 후
# 각 위치마다의 루프를 돌려
# 목표하는 메모리 인덱스 값과 현재 메모리의 인덱스 값이 다를 경우
# 현재 위치부터 끝까지 목표하는 메모리 인덱스의 값으로 변환해주고 정답에 카운팅 해주었다. 

T = int(input())

for test_case in range(1, T + 1):
    memory = list(input())
    present_memory = ['0'] * len(memory)
    
    answer = 0
    
    for i in range(len(memory)):
        if memory[i] != present_memory[i]:
            for j in range(i, len(memory)):
                present_memory[j] = memory[i]
            answer += 1
                
    print('#' + str(test_case), answer)