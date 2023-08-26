# 내가 푼 방식 : 여러 테케 실패 
#               ->  total = sorted(total_genres_dic.items(), key=lambda x:x[1] , reverse=True) 정렬 부분을 
#                   total_genres_dic에서 total_genres_dic.items()로 변경하니 통과됨
# 총 재생횟수의 딕셔너리만 이용해서 각 장르의 총 합을 구하고 큰 순으로 정렬한 후
# 큰 순서의 장르순으로 시작해서 이 때 새로운 각 장르의 값이 들어갈 딕셔너리를 만들고
# 문제에 주어졌던 장르 리스트를 비교하여 같은 장르이면 값을 딕셔너리에 넣고
# 넣어진 딕셔너리에서 큰 순서로 정렬하여
# 각 장르 2개까지이므로 2개까지 큰 순으로 정답에 넣었다.

def solution(genres, plays):
    answer = []
    total_genres_dic = {}                                             # 총 재생횟수의 딕셔너리만 이용해서
    
    for i in range(len(genres)):
        if genres[i] not in total_genres_dic:                          # 각 장르의 총 합을 구하고
            total_genres_dic[genres[i]] = plays[i]
        else:
            total_genres_dic[genres[i]] += plays[i]
        
    total = sorted(total_genres_dic.items(), key=lambda x:x[1], reverse=True)  # 큰 순으로 정렬한 후  (여기서 items()로 정렬하니 정상 통과 됨)
    

    for i, j in total:                                                  # 큰 순서의 장르순으로 시작해서 
        tmp = {}                                                        # 이 때 새로운 각 장르의 값이 들어갈 딕셔너리를 만들고
        
        for j in range(len(genres)):                                    # 문제에 주어졌던 장르 리스트를 비교하여 
            if genres[j] == i:                                          # 같은 장르이면 값을 딕셔너리에 넣고
                tmp[j] = plays[j]
                
        genres_val = sorted(tmp, key=lambda x:tmp[x], reverse=True)     # 넣어진 딕셔너리에서 큰 순서로 정렬하여
        
        for i in range(len(genres_val)):                                # 각 장르 2개까지이므로
            if i == 2:                                                  # 2개까지 큰 순으로 정답에 넣었다.
                break
            answer.append(genres_val[i])
        
    return answer



# 총 재상횟수의 딕셔너리와 장르별 재생횟수&고유번호를 한번에 담은 딕셔너리로 구하는 방식

def solution(genres, plays):
    answer = []
    total = {}    # 장르별 총 재생횟수
    gen_dic = {}  # 장르별 [재생횟수, 고유번호]
    
    for i in range(len(genres)):
        if genres[i] in total.keys():
            total[genres[i]] += plays[i]
            gen_dic[genres[i]].append((plays[i],i))      # [재생횟수, 고유번호]
        else:
            total[genres[i]] = plays[i]
            gen_dic[genres[i]] = [(plays[i],i)]
    
    total = sorted(total.items(), key=lambda x:x[1], reverse=True)
    
    
    for key in total:
        playlist = gen_dic[key[0]]
        playlist = sorted(playlist, key=lambda x:x[0], reverse=True)
        
        for i in range(len(playlist)):
            if i == 2:
                break
            answer.append(playlist[i][1])
            
    return answer