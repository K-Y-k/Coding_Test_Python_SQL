# 내가 시도한 방식 = 런타임 오류

T = int(input())

for test_case in range(10):
    A, B = map(int, input().split())
    answer = 0
    
    for i in range(A, B+1):
        reverse_i = ''
        
        for j in reversed(str(i)):
            reverse_i += j
            
        if i == int(reverse_i):
            root_i = i ** 0.5
            reverse_root_i = ''
            
            for  j in reversed(str(root_i)):
                reverse_root_i += j
            
            if root_i == int(reverse_root_i):
                answer += 1
                
    print('#' + str(test_case), answer)
    



# 루트를 적용할 때 정수이고, [::-1] 활용 방식
# 문제에서 양의 정수이어야 했으므로 루트를 적용한 숫자도 정수화를 해야한다.
# 거꾸로 할 때 [::-1]을 활용하면 더 편하게 가능

T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    answer = 0
    
    for i in range(A, B+1):
        root_i = i ** 0.5
        
        if root_i == int(root_i):
            str_i = str(i)
            str_root_i = str(int(root_i))
            
            if str_i == str_i[::-1] and str_root_i == str_root_i[::-1]:
                answer += 1
                
    print('#' + str(test_case), answer)