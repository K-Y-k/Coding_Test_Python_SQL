# 내가 시도한 방식 = 일부 테케만 맞음

T = int(input())

for test_case in range(1, T + 1):
    num_li = list(map(int, input().split()))

    num_li.sort()
    
    print('#' + str(test_case), ' '.join(map(str, num_li)))