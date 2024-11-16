# 15판 중 o인 것이 8개가 될 수 있다면 YES이므로
# x인 것만 카운트하여 15에서 빼주면 된다.

T = int(input())

for test_case in range(1, T+1):
    result = str(input())

    lose_count = result.count('x')

    answer = 'NO'

    if 15 - lose_count > 7:
        answer = 'YES'


    print('#'+str(test_case), answer)

