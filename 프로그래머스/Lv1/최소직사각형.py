def solution(sizes):
    answer = 0
    
    가로 = []
    세로 = []
    
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]: 
            가로.append(sizes[i][0])
            세로.append(sizes[i][1])
        else:
            가로.append(sizes[i][1])
            세로.append(sizes[i][0])
    
    answer = max(가로) * max(세로)
    
    return answer