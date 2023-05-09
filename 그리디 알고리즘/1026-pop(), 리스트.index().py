# A,B 하나씩 뽑아서 곱하기의 총합을 가장 작게 하려면 (가장 작은수 X 가장 큰수)의 총합을 구하면된다.
# 하지만 A만 재배열을 할 수 있어 A,B를 오름차순 내림차순으로 정렬해서 접근하는 방식은 할 수 없다.
# 그래서 각 A,B 리스트에서 작은 값 큰 값을 하나씩 뽑아서 연산을 적용한 후 pop()으로 제거해준다.


# 정렬 방식 = 실행은 되지만 문제의 의도가 아님
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_a = sorted(A, reverse=True)
sorted_b = sorted(B)

S = 0
for i in range(N):
    S += sorted_a[i] * sorted_b[i]

print(S)


# pop 활용 방식
N = int(input())                       # N번의 입력
A = list(map(int, input().split()))    # A의 리스트 입력 
B = list(map(int, input().split()))    # B의 리스트 입력 
S = 0                                  # 결과 변수 초기화

for i in range(N) :                    # N번의 반복으로 최소값을 출력하기위해 A는 최소 B는 최대로 곱하고 더한다. 

    S += min(A) * max(B)                    

    A.pop(A.index(min(A)))             # pop함수를 이용해서 A배열의 최소값과 B배열의 최대값을 배열에서 빼주는 걸 반복한다.
                                       #  이 방식을 이용하면 B배열을 재배열하지 않아도 s의 최소값을 구할 수 있다.
    B.pop(B.index(max(B)))

print(S)                               # 결과 출력