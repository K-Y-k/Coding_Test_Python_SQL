# 약수 리스트의 약수들이 N의 약수들이라고 했으므로
# N의 값을 구하려면 약수 리스트의 가장 작은 값과 가장 큰 값을 곱한 값이다.
# 그래서 정렬 처리한 후 첫째항과 끝의항을 곱하였다.

count = int(input())
A_li = list(map(int, input().split()))
A_li.sort()

N = A_li[0] * A_li[-1]

print(N)