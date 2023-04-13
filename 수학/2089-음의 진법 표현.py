# 메커니즘 : -2로 나누어 떨어지지 않을 때의 몫이 소수점이 되는데 
#            몫에 소수점을 버리고 +1을 해야 이 메커니즘이 계속 진행가능하다. 
# ex)
# -13 = -2*(7) + 1

#   7 = -2*(-3) + 1

#  -3 = -2*(2) + 1

#   2 = -2*(-1) + 0

#  -1 = -2*(1) + 1

#   1 = -2*(0) + 1



minus_ = int(input())

minus_binary = []

if not minus_:
    print(0)
    exit()

while minus_:
    if minus_ % -2 != 0:           # 나누어 떨어지지 않은 경우 
        minus_binary.append(1)
        minus_ = minus_//-2 + 1    # 위 메커니즘 때문에 몫에 +1을 해줘야한다
    else:
        minus_binary.append(0)
        minus_ //= -2
        
for i in reversed(minus_binary):   # 마지막에 들어간 수부터 나와야하므로 역으로 뒤집어서 출력
    print(i, end="")