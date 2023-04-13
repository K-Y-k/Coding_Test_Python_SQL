a = input().split('-')       # 최소값으로 만들기 위한 괄호는 -기준으로 씌워져야하기에 -기준으로 분리한다.
result = 0                   # 결과 변수 초기화

for i in a[0].split('+') :   # 첫 원소는 무조건 +이므로 따로 +연산을 실시  +가 있을 수 있어 +기준으로 분리 후 합 
    result += int(i)

for i in a[1:] :             # 분리된 기준이 -였으므로 +가 있을 수 있으니 +로 분리 후 그 값들 모두 -로 연산해준다.
    for j in i.split('+') :
        result -= int(j)

print(result)                # 결과 출력