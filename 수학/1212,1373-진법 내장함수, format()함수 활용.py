# 1373번 : 2진수 -> 8진수
# 내장함수로 진법 변환  방식
bin_ = int(input(), 2)   # 2진법으로 표현 

o = oct(int(bin_))[2:]   # 8진법 변환 내장함수 oct() (내부에 int(bin_)인 것은 2진법을 10진법으로 변환하고 적용해야하므로)

print(o)


# format함수로 진법 변환 방식
bin_ = int(input(), 2)

o = format(int(bin_), 'o')    # 'o'로 8진법 변환

print(o)



# 1212번 : 8진수 -> 2진수
# 내장함수로 진법 변환  방식
oct_ = int(input(), 8)       # 8진법으로 표현 

b = oct(int(bin_))[2:]       # 2진법 변환 내장함수 bin()

print(b)


# format함수로 진법 변환 방식
oct_ = int(input(), 8)

b = format(int(oct_), 'b')   # 'b'로 2진법 변환

print(b)