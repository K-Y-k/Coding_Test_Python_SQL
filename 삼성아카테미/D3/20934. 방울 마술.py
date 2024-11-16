# 'o'인 방울이 울린 횟수인 K 만큼만 반복하여
# 'o'인 곳을 찾고 문제 조건에 따라서 섞어주었다.
# 그 후 'o'이 있는 인덱스를 찾아준다.

T = int(input())

for test_case in range(1, T+1):
    S, K = map(str, input().split())
    S = list(S)
    answer = 0

    for _ in range(int(K)):
        for i in range(len(S)):
            if S[i] == 'o':
                if i == 0:
                    S[i] = '.'
                    S[i+1] = 'o'
                else:
                    S[i] = '.'
                    S[i-1] = 'o'
                break

    answer = S.index('o')

    print('#' + str(test_case), answer)
