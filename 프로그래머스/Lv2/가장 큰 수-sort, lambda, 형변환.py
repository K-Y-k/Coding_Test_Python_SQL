# 내가 푼 방식 : 시간 초과 발생
# 순열을 이용하여 각 주어진 숫자들이 합친 경우의 수를 조회하면서
# 큰 수를 찾아내었다.

from itertools import permutations

def solution(numbers):
    answer = ''
    
    p = permutations(numbers, len(numbers))          # 순열을 이용하여 
    max_numbers = 0
    
    for i in p:                                      # 각 주어진 숫자들이 합친 경우의 수를 조회하면서
        a = ''.join(map(str,i))
        
        if int(a) > max_numbers:                     # 큰 수를 찾아내었다.
            max_numbers = int(a)
        
    answer = str(max_numbers)
    

    return answer



# 정렬을 활용한 방식
# 문제에서 numbers의 원소 값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하면 큰 수를 찾을 수 있으므로
# 현재 숫자에 같은 숫자를 3번 이어붙이면 큰 수로 찾아낼 수가 있다.

def solution(numbers):
    answer = ''
    
    str_num = []                                     # 정렬 람다 비교에서 같은 숫자를 3번 붙여야하므로 원소가 문자열인 것으로 다시 생성
    for i in numbers:
        str_num.append(str(i))
    
    str_num.sort(key=lambda x: (x*3), reverse=True)  # 현재 숫자 x를 3번씩 반복하여 붙였을때 큰 수 찾기 가능
    answer = str(int(''.join(str_num)))              # 문자열 000 같은 경우의 반례를 대비하여 숫자형으로 한번 바꾸어 0으로 만들고 나서 다시 문자열로 바꾼 것
    

    return answer