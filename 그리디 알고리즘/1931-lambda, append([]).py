N = int(input())                                # 회의 수 입력

conference_time = []

for _ in range(N):                              # 0부터 시작이므로 N+1번 반복
    start, end = map(int, input().split())      # 시작시간 끝시간을 공백을 기준으로 나누어 저장
    conference_time.append([start, end])        # [ ]로 append 가능하다. 

conference_time = sorted(key=lambda x: x[0])    # 시작 시간을 기준으로 오름차순
conference_time = sorted(key=lambda x: x[1])    # 끝 시간 기준으로 다시 오름차순


last = 0                                        # 회의의 마지막 시간을 저장할 변수
count = 0                                       # 회의 개수를 저장할 변수

for i, j in conference_time:
  if i >= last:                                 # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    count += 1                                  # 회의 개수를 증가하고 마지막 시간을 최신으로 갱신
    last = j

print(count)