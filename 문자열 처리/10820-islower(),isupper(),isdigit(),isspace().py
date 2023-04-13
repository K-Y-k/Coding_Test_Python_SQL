while True:
    try:
        lower = 0
        upper = 0
        num = 0
        blank = 0
        
        word_l = input()
        
        for i in word_l:
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            elif i.isdigit():
                num += 1
            elif i.isspace():
                blank += 1
            
        print(lower, upper, num, blank)
        
    except EOFError:
        break