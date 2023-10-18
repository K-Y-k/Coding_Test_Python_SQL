T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    
    operation = ''
    
    if a < b:
        operation = '<'
    elif a > b:
        operation = '>'
    else:
        operation = '='

    print('#' + str(test_case), operation)
    