# 점수들을 리스트에 담고
# 각 점수들을 조회해서 40점 미만은 40점으로 다시 만들어준 후
# 평균을 구하고 출력한다.  

T = int(input())

for test_case in range(1, T + 1):
    score_li = list(map(int, input().split()))
    
    for i in range(len(score_li)):
        if score_li[i] < 40:
            score_li[i] = 40
    
    avg = sum(score_li) // len(score_li)
    
    print('#' + str(test_case), avg)
