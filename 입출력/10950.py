import sys
N = int(input())

for _ in range(N) :
    A, B = map(int, sys.stdin.readline().split())  # 반복문 안에서의 입력은 sys.stdin.readline()이 바람직함, split으로 공백 구분 입력
    print(A+B)


# 테스트 케이스 형식으로 주어지는 경우 각각을 독립적인 문제로 생각하고 풀면 된다.
# 전체 테스트 케이스를 입력 받은 다음에 풀지 않아도 된다.