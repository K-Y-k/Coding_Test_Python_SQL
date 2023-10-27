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
