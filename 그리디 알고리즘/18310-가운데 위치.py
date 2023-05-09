N = int(input())

position = list(map(int, input().split()))

position.sort()                               # 오름차순 정렬
result = 0

if len(position) % 2 == 0:                    # 입력한 리스트 전체길이가 짝수이면 전체길이/2
    result = len(position)//2
else:                                         # 입력한 리스트 전체길이가 홀수이면 전체길이/2 후 +1
    result = len(position)//2 + 1 
    
print(position[result-1])