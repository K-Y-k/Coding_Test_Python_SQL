def solution(n, arr1, arr2):
    answer = []
    
    a_arr1 = []
    b_arr2 = []
    
    for i in arr1:
        a = bin(i)[2:]
        val = a.zfill(n)
        a_arr1.append(val)
        
    for i in arr2:
        b = bin(i)[2:]
        val = b.zfill(n)
        b_arr2.append(val)
    
    for i in range(len(a_arr1)):
        temp = ''
        
        for j in range(n):
            if a_arr1[i][j] == '1' or b_arr2[i][j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    
    return answer