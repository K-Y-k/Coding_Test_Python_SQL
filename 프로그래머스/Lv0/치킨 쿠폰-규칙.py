# 내가 푼 방식 : 테스트케이스 하나 실패
# 치킨이 10개 미만이 될 때까지 
# 현재 치킨에 10으로 나누어 해당 값이 서비스 치킨 개수가 되고
# 현재 치킨에 10으로 나눈 나머지가 쿠폰 개수로 카운팅하면서 진행했다.

def solution(chicken):
    answer = 0
    coupon = 0
    
    while chicken >= 10:                        # 치킨이 10개 미만이 될 때까지 
        service_chicken = chicken // 10         # 현재 치킨에 10으로 나누어 해당 값이 서비스 치킨 개수가 되고
        
        answer += service_chicken
        coupon += chicken % 10                  # 현재 치킨에 10으로 나눈 나머지가 쿠폰 개수로 카운팅하면서 진행했다.
        
        if service_chicken < 10:                # 치킨이 10개 미만인 경우 다음 반복이 진행이 안되므로 
            coupon += service_chicken           # 그 개수까지 쿠폰에 미리 적용
        
        if coupon >= 10:                        # 쿠폰이 10개 이상일 때
            answer += coupon // 10              # 서비스 치킨을 주문
            coupon = coupon % 10                # 남은 잔여량도 적용
            
        chicken = service_chicken
    

    return answer



# 깔끔한 풀이
# 처음 쿠폰의 초깃값을 치킨 개수로 시작하고 
# 쿠폰의 개수를 잔여량 + 현재 서비스 치킨으로 주문한 것까지 쿠폰에 합해주면 끝이었다. 

def solution(chicken):
    answer = 0
    coupon = chicken                                # 처음 쿠폰의 초깃값을 치킨 개수로 시작하고 
    
    while coupon >= 10:                             # 쿠폰이 10개부터 서비스 치킨 주문이 가능하므로 10개이상일 때까지 반복하여
        service_chicken = coupon // 10              # 서비스 치킨을
        answer += service_chicken                   # 카운팅하고
        
        coupon = coupon % 10 + service_chicken      # 쿠폰의 개수를 잔여량 + 현재 서비스 치킨으로 주문한 것까지 쿠폰에 합해주면 끝이었다. 
    

    return answer