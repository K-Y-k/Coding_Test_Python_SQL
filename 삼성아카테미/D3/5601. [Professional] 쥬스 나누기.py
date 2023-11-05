# 문제 설명이 결국 따른사람이 바로 가져가는 것이 아닌 따르고 난후의 잔들에서 가져가는 것이므로
# 최대한의 전략이라고 했으므로 1L/모든 사람으로 분배하는 것이 최선이다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    answer = []
    
    for i in range(N):
        answer.append('1'+'/'+str(N))
    
    print('#' + str(test_case), ' '.join(answer))
   