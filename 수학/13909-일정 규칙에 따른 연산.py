# 내가 푼 방식 - 메모리 초과
# 입력한 값만큼 리스트에 0의 요소로 초기화 해놓은 다음
# 1부터 입력 값까지 반복해서 각 인덱스가 현재 값에 나누어 떨어지면 해당되는 인덱스이므로 처리해주었다.

# 하지만 문제에서 창문의 개수와 사람의 수 N(1 ≤ N ≤ 2,100,000,000)로 최대 크기가 너무 커서
# 반복 처리가 불가능

N = int(input())
num_li = [0 for i in range(1, N+1)]


for i in range(1, N+1):
    for j in range(N):
        if (j+1) % i == 0:
            if num_li[j] == 0:
                num_li[j] = 1
            else:
                num_li[j] = 0


print(num_li.count(1))



# 주어진 값에 따른 일정 패턴이 있었다.
# 일부 숫자의 결과를 보면 입력 값의 제곱 수임을 알 수 있다.

N = int(input())

print(int(N**0.5))