# 0~9의 숫자를 저장할 카운트 리스트를 생성하고
# 카운트 리스트가 10개가 될 때까지 각 배수를 곱하면서 0~9의 숫자가 모두 들어가게 반복한다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    count_li = []
    answer_count = 0
    multi_count = 1
    
    
    while True:
        if len(count_li) == 10:
            break
        
        a = N * multi_count
        
        for i in str(a):
            if i not in count_li:
                count_li.append(i)
            
            
        multi_count += 1
        answer_count = a
        

    print('#' + str(test_case), answer_count)