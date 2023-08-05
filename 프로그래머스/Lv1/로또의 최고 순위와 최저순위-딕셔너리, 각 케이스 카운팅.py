# 내가 푼 방식
# 일치하는 로또의 개수에 따른 등수를 딕셔너리를 담고
# 최대가 될 수 있는 로또 개수와 최소가 될 수 있는 로또 개수를 각 카운팅 처리하였고
# 일치 개수의 값이 등수로 저장했으므로
# 일치 개수의 값인 등수를 정답에 넣기


def solution(lottos, win_nums):
    answer = []
    
    rank_dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} # 일치하는 로또의 개수에 따른 등수를 딕셔너리를 담고
    max_lottos = 0
    min_lottos = 0
    
    for i in lottos:                  
        if i in win_nums or i == 0:                # 최대가 될 수 있는 로또 개수 카운팅
            max_lottos += 1
        
        if i in win_nums:                          # 최소가 될 수 있는 로또 개수 카운팅
            min_lottos += 1
    
    answer.append(rank_dic[max_lottos])            # 일치 개수의 값인 등수를 정답에 넣기
    answer.append(rank_dic[min_lottos])

    
    return answer