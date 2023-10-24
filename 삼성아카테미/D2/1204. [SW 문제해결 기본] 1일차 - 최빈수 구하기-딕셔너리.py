T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_li = list(map(int, input().split()))
    
    num_dic = {}
    
    for i in num_li:
        if i in num_dic:
            num_dic[i] += 1
        else:
            num_dic[i] = 1
    
    max_count = 0
    answer = 0
    
    for key, value in num_dic.items():
        if value > max_count:
            answer = key
            max_count = value
        elif value == max_count:
            if key > answer:
                answer = key
    
    print('#' + str(N), answer)