# 주의점: 슬라이스[시작:끝]은 끝의 원소값은 포함안됨!
# 같은 패턴이 이어지려면 현재 위치의 원소에서의 값이 x2를 한 위치의 원소의 값과 동일해야한다! 

T = int(input())

for test_case in range(1, T + 1):
    pattern_li = str(input())
    
    
    for i in range(len(pattern_li)):
        if pattern_li[:i+1] == pattern_li[i+1:(i+1)*2]:
            print('#' + str(test_case), i+1)
            break