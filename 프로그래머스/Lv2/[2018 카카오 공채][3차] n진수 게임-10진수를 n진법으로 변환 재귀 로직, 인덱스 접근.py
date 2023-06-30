# 10진법 -> n진법으로 변환하는 로직은 외워두자!

def convert(n, base):                        # n을 base진법으로 변환 함수
    T = "0123456789ABCDEF"                   # "0123456789ABCDF" 문자열을 생성
    q, r = divmod(n, base)                   # n을 base로 나눈 몫과 나머지를 구한다.
    
    if q == 0:                               # 몫이 0이면 생성해 둔 문자열의 나머지 인덱스를 리턴한다.
        return T[r]
    else:                                    # 0이 아니라면 convert(몫, base)를 재귀호출하고, T의 나머지 인덱스를 붙인다.
        return convert(q, base) + T[r]

    
def solution(n, t, m, p):
    answer = ''                             
    temp = ''                                # 변환된 진법을 차례로 이어붙일 변수 선언
    
    for i in range(t*m):                     # 최대 크기 범위는 말해야 하는 숫자의 t개 x 참여자 수인 m명이다.
        temp += str(convert(i, n))           # 진법 변환하고 문자열에 이어붙인다. 
        
    
    while len(answer) < t:                   # 말해야하는 숫자 t개가 될 때까지 반복하여
        answer += temp[p-1]                  # 원소 인덱스는 0부터 시작하므로 정답에 현재 순서-1의 위치하는 값을 넣는다. 
        p += m                               # 현재 순서를 참여자 수만큼 더하여 다음 자기 차례인 순서로 만든다.
    
    return answer