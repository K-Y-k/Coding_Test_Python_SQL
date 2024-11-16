# 하나의 리스트의 값들을 2개의 리스트로 절반씩 나눈 후 순차대로 하나씩 넣는다.
# 단 전체 길이가 홀수일 경우와 짝수의 경우 처리를 따로 해주어야 한다.

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    word_li = list(map(str, input().split()))

    A = []
    B = []

    answer = []

    if N % 2 == 1:
        A = word_li[:N//2+1]
        B = word_li[N//2+1:]

        for i in range(len(B)):
            answer.append(A[i])
            answer.append(B[i])

        answer.append(A[-1])
    else:
        A = word_li[:N//2]
        B = word_li[N//2:]

        for i in range(len(A)):
            answer.append(A[i])
            answer.append(B[i])

    print('#' + str(test_case), ' '.join(answer))
