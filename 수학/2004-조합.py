# 순열 공식 = nPr이면  n! / (n-r)!
# 조합 공식 = nCr이면 n! / ((n-r)! * r!)
 
# 내가 푼 시간 초과가 발생하는 fatorial 방식
import math

n, m = map(int, input().split())

result = math.factorial(n) // math.factorial(m) // math.factorial(n-m)

count = 0

for i in reversed(str(result)):
  if i != '0':
    break
  else:
    count += 1

print(count)



# 시간초과 방지 방식 : 끝자리부터 0이 연속으로 오는 개수를 찾는 것이므로 팩토리얼에서 0을 만들 수 있는 2와 5의 개수를 기준으로 찾기
# 0의 개수 = n!가 가지고 있는 2의 개수 - r!이 가지고 있는 2의 개수 - (n-r)!이 가지고 있는 2의 개수
#           와 
#           n!가 가지고 있는 5의 개수 - r!이 가지고 있는 5의 개수 - (n-r)!이 가지고 있는 5의 개수
#           중 작은 수

def countNum(N, num):
    count = 0

    divNum = num

    while N >= divNum:
        count = count + (N // divNum)
        divNum = divNum * num

    return count

n, m = map(int, input().split())
print(min(countNum(n, 2) - countNum(m, 2) - countNum(n-m, 2), countNum(n, 5) - countNum(m, 5) - countNum(n-m, 5)))