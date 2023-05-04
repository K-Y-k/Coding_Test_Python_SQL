# 0~9999까지 에라토스테네스의 체를 활용해 소수인 것을 미리 찾아놓고
# 각 자리의 수(0~9)를 바꿔가며 소수인 수는 큐에 넣어서 또 다시 자릿수를 바꾸어 가며 
# 바꾸어야 하는 숫자가 나올 때 판별한다. 

# 또한 큐에 넣은 숫자는 방문처리를 하여 중복된 카운트를 방지한다.

# 이때 바꾸어야하는 숫자의 조건
# : 1.해당숫자가 이미 방문해서 카운트를 했던건 아닌지
#   2.소수인지
#   3.문제에서 4자리 수만이라고 했으므로 1000이상인지도 판별


from collections import deque
import sys

def findPrime():                        # 에라토스테네스의 체
    for i in range(2, 10000):           # 2부터 문제에서 주어진 최대값(9999)까지 조회
        if prime[i] == True:            # 소수이면
            j = i*i                     # i x i를 해서
        
        while j < 10000:                # i x i가 최대 값보다 작을 때까지
            prime[j] = False            # 배수들은 False로 지워줘 결국 True인 것은 소수만 남을 것이다.
            j += i                      # i*(i+1)식으로 증가해야 하므로 i를 더한 것이다.


def bfs(start, end):                    # 시작 값, 끝의 값을 받아온 BFS함수
    q = deque()                         # deque선언
    q.append((start, 0))                # 시작 값, 현재 카운트된 회수 0부터 넣고 
    visited[start] = True               # 위 시작 값을 넣었으므로 방문처리 
    
    while q:                            # 큐가 빌 때까지
        now, count = q.popleft()        # 현재값, 현재까지의 카운트 회수 꺼내와서

        if now == end:                  # 만약 끝의 값까지 도달했으면
            return count                # 현재까지의 카운트 회수를 반환
        
        strNow = str(now)               # 현재값을 문자열로 변환

        for i in range(4):                                            # 각 자리수(4자리수)만큼 반복하고 
            for j in range(10):                                       # 그 자리수의 올 수 있는 숫자(0~9)를 반복하여 차례로 조회
                temp = int(strNow[:i] + str(j) + strNow[i+1:])        # 각 자리수 때문에 문자열로 변환하여 끼워넣고 다시 숫자로 변환
                
                if not visited[temp] and prime[temp] and temp>=1000:  # 바꾸어야하는 숫자 조건 3가지에 달성했으면
                    visited[temp] = True                              # 방문처리를 해주고
                    q.append((temp, count+1))                         # 바꾸어야하는 숫자, 현재까지의 회수 + 1로 큐에 넣어준다.
                    
    return 'impossible'                                               # 큐가 빌 때까지 끝의 값까지 도달하지 못했으면 불가능한 경우로 impossible 반환


T = int(input())                                                      # 테스트 케이스 입력

prime = [True for _ in range(10000)]                                  # 소수판별을 위한 배열 초기화
prime[0] = prime[1] = False                                           # 0과 1은 소수가 아니므로 미리 False로 초기화
findPrime()                                                           # 에라토스테네스의 체로 소수들만 True로 적용함

for _ in range(T):                                                    # 입력한 테스트 케이스만큼 반복
    start, end = map(int, sys.stdin.readline().rstrip().split())      # 시작 값, 끝의 값을 입력
    visited = [False for _ in range(10000)]                           # 방문여부를 초기화
    
    print(bfs(start, end))                                            # BFS함수를 시작하여 반환된 값 출력