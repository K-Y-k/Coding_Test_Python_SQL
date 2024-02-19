# k명까지 상을 받는다 했으므로 
# 내림차순으로 역순정렬한 후 커트라인인 k번째의 값을 출력

N, k = map(int, input().split())

score_li = list(map(int, input().split()))
score_li = sorted(score_li, reverse=True)

print(score_li[k-1])