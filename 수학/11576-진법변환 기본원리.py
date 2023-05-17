A, B = map(int, input().split())

A_m = int(input())

A_list = list(map(int, input().split()))

AToTen = 0

A_list.reverse()                             # 아래자리부터 구하기 위해 역으로 뒤집음

for i in range(0, len(A_list)):
    AToTen += A_list[i]*(A**i)               # N진법->10진법으로 변환은 각 자리수 * N진법의 n거듭제곱 형태이므로  ex) 17제곱인 각자리 2 16이 10진법으로 바꾸려면 2*(17**1)+16*(17**0) 

tenToB = []
    
while AToTen:                                # !=0까지 반복
    tenToB.append(AToTen % B)                # 기본적인 10진수->N진법으로 변환 원리는 해당 10진법 수를 N진법으로 나눈 나머지를 최근 넣은순으로 차례로 나온 값이다.
    AToTen //= B 


for i in reversed(tenToB):                   # 최근 넣은순으로 나와야하므로 reversed
    print(i, end=' ')

# 위 출력을 join방식으로 한것
tenToB.reverse()
print(' '.join(map(str, tenToB)))           # 문자열 리스트만 join이 가능하여 숫자형을 문자열로 형 변환