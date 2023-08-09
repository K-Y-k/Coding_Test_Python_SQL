# 시도한 방식 : 일부 테스트 케이스 실패
# index()로 이름 부른 플레이어의 인덱스를 찾고 
# 그 앞의 플레이어와 스왑을 하는 방식을 생각했다.
# 하지만 index()로 인덱스를 찾는 연산이 시간복잡도가 높아 시간초과가 발생함

def solution(players, callings):
    answer = []
    
    for present_player in callings:
        idx = players.index(present_player)     # index()로 이름 부른 플레이어의 인덱스를 찾고 
        before_player = players[idx-1]         
        
        players[idx-1] = present_player         # 그 앞의 플레이어와 스왑
        players[idx] = before_player 
    
    answer = players
    
    return answer



# 그래서 딕셔너리를 사용해서 대용량에 데이터에서 빠르게 인덱스를 찾을 수 있게 해야 한다.

def solution(players, callings):
    answer = []
    rank_dic = {}
    
    for i, value in enumerate(players):        # 차례로 딕셔너리에 순위 적용
        rank_dic[value] = i
    
    for present_player in callings:
        idx = rank_dic[present_player]         # 그래서 딕셔너리를 사용해서 대용량에 데이터에서 빠르게 인덱스를 찾을 수 있게 해야 한다.
        before_player = players[idx-1]
        
        rank_dic[present_player] -= 1          # 딕셔너리 순위 최신화 적용
        rank_dic[before_player] += 1
        
        players[idx-1] = present_player        # 그 앞의 플레이어와 스왑
        players[idx] = before_player  
    
    answer = players
    
    return answer