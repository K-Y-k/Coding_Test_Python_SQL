# 일일히 append 방식 = 메모리 초과

import sys

N = int(input())

num_li = []

for _ in range(N):
    num_li.append(int(sys.stdin.readline()))

num_li.sort()

for i in num_li:
    print(i)



# 배열로 미리 할당 방식
# for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용못한다.
# 일반적으로 입력값이 크지않은 경우에는 상관없지만
# 입력값 범위가 극한으로 많이 주어질 때에는 메모리를 좀 더 효율적으로 관리해야한다.

# 그래서 입력값이 10000개 까지 주어질 수 있으니 10000개 만큼의 리스트를 만들어 놓는다.
# 리스트에 각 요소마다 0을 할당해놓고 입력값을 받을 때마다 그 입력값과 같은 인덱스에 +1씩 해준다.
# 입력을 다 받고나면 0보다 큰 요소를 갖는 인덱스들을 찾아서 그 수만큼 인덱스를 출력해주면 된다.

import sys

N = int(input())

num_li = [0] * 10001

for i in range(N):
    num_li[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_li[i] != 0:
        for j in range(num_li[i]):
            print(i)

