# sort()로 정렬한 후 join으로 리스트 한번에 출력

T = int(input())

for test_case in range(1, T + 1):
    num_li = list(map(int, input().split()))

    num_li.sort()
    
    print('#' + str(test_case), ' '.join(map(str, num_li)))