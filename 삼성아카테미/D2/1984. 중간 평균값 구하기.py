T = int(input())

for test_case in range(1, T + 1):
    num_li = list(map(int, input().split()))
    
    num_li.sort()                             # 정렬 후
    num_li.pop(0)                             # 최솟값 제거 방식 
    num_li.pop()                              # 최댓값 제거 방식

    # num_li.remove(max(num_li))
    # num_li.remove(min(num_li))
    
    avg = sum(num_li) / len(num_li)
    
    print('#' + str(test_case), round(avg))