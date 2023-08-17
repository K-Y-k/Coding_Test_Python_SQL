# 중복 순열 활용 방식
# product(반복 객체, 반복 개수)로 중복인 숫자가 올 수 있고 순서가 다르면 다른 경우의 수로 인식하는 순열을 이용할 수 있다.
# 문제에서 나열 순서가 결국 문자열 오름차순이랑 똑같다. 이 때문에 처음부터 나열된 상태로 넣을 필요가 없다.

from itertools import product

def solution(word):
    answer = 0
    
    dic_li = []
    dic = ['A', 'E', 'I', 'O', 'U']
    
    
    for i in range(1, 6):
        p = product(dic, repeat=i)               # product(반복 객체, 반복 개수)로 중복인 숫자가 올 수 있고 순서가 다르면 다른 경우의 수로 인식하는 중복 순열을 이용할 수 있다.
        
        for j in p: 
            dic_li.append(''.join(j))
        

    dic_li.sort()                                # 문제에서 나열 순서가 결국 문자열 오름차순이랑 똑같다. 이 때문에 처음부터 나열된 상태로 넣을 필요가 없는 것!

    answer = dic_li.index(word) + 1              # 인덱스가 0부터 시작했으므로
    

    return answer


# 일일히 루프를 돌아 다 넣어보는 방식
# 문제에서 주어진 단어 수에서의 경우의 수가 1억 경우의 수보다 적기에 일일히 넣을 수 있다.
# 단, 똑같은 단어가 있을 수 있어 검사해야한다.

from itertools import product

def solution(word):
    answer = 0
    
    dic_li = []
    dic = ['A', 'E', 'I', 'O', 'U', '']
    

    # 문제에서 주어진 단어 수에서의 경우의 수가 1억 경우의 수보다 적기에 일일히 넣을 수 있다.        
    for i in dic:
        for j in dic:
            for l in dic:
                for m in dic:
                    for n in dic:
                        temp = i+j+l+m+n
                        if temp not in dic_li:     # 단, 똑같은 단어가 있을 수 있어 검사해야한다.
                            dic_li.append(temp)
        

    dic_li.sort()    

    answer = dic_li.index(word)
    

    return answer