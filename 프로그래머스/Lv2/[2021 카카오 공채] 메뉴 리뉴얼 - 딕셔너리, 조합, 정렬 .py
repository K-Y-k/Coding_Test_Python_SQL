# 각 코스 길이별로 주문한 카운팅이 제일 큰값인 것만 담는다.
# 즉, 문제에서 원하는 코스 길이일 때의 리턴을 기준으로 조회하고
# 그 길이에 맞게 카운팅하고 카운팅한 것중 가장 큰 값인 것들만 담는다.
# 그리고 문자순으로 출력되므로 마지막에 문자를 기준으로 정렬 처리를 해준다. 


from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in course:               # 전체를 만들 필요없이 문제에서 각 코스의 길이 만큼의 기준으로만 구하면 답이 나오므로 코스 길이별로 조회
        order_dic = {}             # 각 조합의 카운팅을 확인하기 위한 딕셔너리 선언
        
        for order in orders:       # 주문을 하나씩 조회
            combination_order = combinations(sorted(order), i) # 위 코스의 길이를 기준으로 조합 구하기 + 문제에서 XY와 YX가 같은 것인데 출력을 XY로 문자 기준으로 출력하고 싶어하므로 정렬을 하고 조합을 진행해야한다.
            
            for j in combination_order: # 조합을 조회해서
                if j not in order_dic:  # 만약 딕셔너리에 없다면
                    order_dic[j] = 1    # 카운팅을 새로 해주고

                else:                   # 이미 있으면
                    order_dic[j] += 1   # 기존꺼에 카운팅해준다.
        
        
        count = []                       # 카운팅한 것만 담아두기 위한 리스트 선언
        
        for key in order_dic:            # 위 카운팅한 딕셔너리를 조회해서
            count.append(order_dic[key]) # 카운팅 리스트에 넣기
        
        for key in order_dic:            # 다시 딕셔너리를 조회해서
            if order_dic[key] > 1 and order_dic[key] == max(count): # 2번이상 주문한 것이고 카운팅 리스트에서 최대 값일 경우 가장 많이 주문한 것이므로
                temp = ''.join(key)                                 # 딕셔너리에 ['A', 'B']처럼 담겨있으므로 하나로 통일하기 위한 과정
                answer.append(temp)
        
                
    answer.sort()                        # 문제에서 답이 문자순으로 출력되므로 문자를 기준으로 정렬 처리를 해준 것
            
    
    return answer