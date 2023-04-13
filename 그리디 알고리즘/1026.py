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