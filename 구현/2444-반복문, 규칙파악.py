# 공백과 별의 개수의 규칙을 파악하고
# 반복문이 가능한 범위로 따로 분류하는 것이 핵심이다.

N = int(input())

for i in range(1, N+1):
    print(" "*(N-i) + "*"*(2*i-1))
    
for j in range(N-1, 0, -1):
    print(" "*(N-j) + "*" * (2*j-1))