# 내가 푼 방식
# 정렬을 한 후 인용횟수가 현재 값보다 큰 경우 카운팅하여 
# 최종 카운팅 한 것이 문제에서 주어진 조건에 갖추었을 경우 최종 인용로 갱신해나가게 했다. 


def solution(citations):
    h = 0                                                          # 인용 횟수의 최대 값을 넣을 변수 선언
    citations.sort()                                               # 오름차순 정렬
    
    for i in range(0, max(citations)+1):                           # 최대 값까지 조회 
        h_count = 0                                                # 현재 인덱스에서의 인용되는 카운팅 변수 선언 및 초기화
        
        for j in citations:                                        # 인용 리스트를 조회해서
            if j >= i:                                             # 인용 리스트의 인용횟수가 현재 인용하는 값보다 크거나 같으면 
                h_count += 1                                       # 현재 인용횟수에 카운팅
                
        if h_count >= i and len(citations)-i <= h_count and i > h: # 문제에서 주어진 조건인 h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면과 현재 인용 기준 값이 최종 인용 값보다 크면
            h = i                                                  # 최대 값으로 갱신
        
    
    return h