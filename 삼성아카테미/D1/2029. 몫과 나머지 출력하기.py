T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    
    c, d = divmod(a, b)
    
    print('#' + str(test_case), c, d)