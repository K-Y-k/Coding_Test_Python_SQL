N, L = map(int, input().split())        # 수리해야할 파이프 개수 N, 테이프 길이 L

pipe = list(map(int, input().split()))  # 위 입력한 개수 만큼 파이프 위치

pipe.sort()                             # 오름차순으로 정렬

start = pipe[0] - 0.5                   # 첫 기준 값은 첫 파이프 위치의 -0.5
count = 1                               # 첫 기준 카운트 값은 최소 1부터 시작

for i in range(1, len(pipe)):           # 위 첫 파이프 위치를 지정했으므로 다음 파이프부터 비교
    if start + L >= pipe[i] + 0.5:      # 기준 값 + 테이프 길이가 다음 파이프 위치 + 0.5보다 크면
        continue                        # 기존 테이프로 붙이므로 카운트 증가 없이 넘어감
        
    else:                               # 기준 값 + 테이프 길이보다 다음 파이프 위치가 넘어서면
        start = pipe[i] - 0.5           # 기준 값을 다음 파이프 위치 -0.5로 갱신하고
        count += 1                      # 테이프를 새로 붙여야하므로 카운트를 +1한다.
        
print(count)

