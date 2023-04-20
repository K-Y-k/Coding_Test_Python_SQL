def solution(bin1, bin2):
    answer = 0
    s = ''
    
    reverse_bin1 = list(map(int, bin1))
    reverse_bin2 = list(map(int, bin2))
    
    reverse_bin1.reverse()
    reverse_bin2.reverse()


    a = 0
    b = 0
    
    for i in range(len(reverse_bin1)):
        a += reverse_bin1[i] * 2**(i)
        
    for i in range(len(reverse_bin2)):
        b += reverse_bin2[i] * 2**(i)
        
        
    answer = a + b
    
    while True:
        if answer // 2 == 0:
            s += str(answer % 2)
            break
            
        s += str(answer % 2)
        answer //= 2
        
    s = list(s)
    s.reverse()
    s = ''.join(s)
    
    return s