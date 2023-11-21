# 케이스에 따른 분류를 했다.
# 1. n 보다 s가 작으면 n개의 자연수의 합으로 s 값을 만들 수 없는 케이스
# 2. 만들 수 있을 때 n개의 자연수의 합이 최대한 가운데의 값으로 구성되어야 최대 곱셈이다.
#    2-1. 나머지가 없을 경우 n개로 나눈 값으로 n개가 형성된 값들이 정답이고
#    2-2. 나머지가 있을 경우 n개로 나눈 나머지의 값을 1씩 n개의 값들에 더해준 값들이 정답 


def solution(n, s):
    answer = []

    if n > s:                            # 1. n 보다 s가 작으면 n개의 자연수의 합으로 s 값을 만들 수 없는 케이스
        answer.append(-1)
    else:                                # 2. 만들 수 있을 때 n개의 자연수의 합이 최대한 가운데의 값으로 구성되어야 곱셈이 가장 커지므로
        if s % n == 0:                   #    2-1. 나머지가 없을 경우 n개로 나눈 값으로 n개가 형성된 값들이 정답이고
            for _ in range(n):
                answer.append(s//n)
        else:
            for _ in range(n):          #    2-2. 나머지가 있을 경우
                answer.append(s//n)

            count = s % n               #          n개로 나눈 나머지의 값을
            for i in range(count):      #          1씩 n개의 값들에 더해준 값들이 정답 
                answer[i] += 1

            answer.sort()               #          정답이 오름차순이므로 마지막에 정렬해줌


    return answer