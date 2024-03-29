nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Z가 35이므로 36진법까지 표현가능

N, B = map(int, input().split())

result = ''

while N > 0:
    result += nums[N % B]                      # 나머지의 값이 nums의 나머지 값의 위치와 동일하므로 이렇게 구현가능
    N //= B
    
print(result[::-1])                            # 먼저 들어간 값이 끝에서 나와야하므로 뒤에서부터 출력