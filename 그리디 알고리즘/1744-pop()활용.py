import sys

N = int(input())

positive_number_list = []
nagative_number_list = []

result = 0

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 1:                               # 1일 때는 곱하지 않고 더하는게 더 큰 값이 나오므로 미리 더해줌
        result += 1
    elif x > 0:                              # 양수는 양수 리스트에 넣기
        positive_number_list.append(x)
    else:                                    # 음수는 음수 리스트에 넣기
        nagative_number_list.append(x)

positive_number_list.sort();                 # 양수는 오름차순으로 정렬
nagative_number_list.sort(reverse=True)      # 음수는 내림차순으로 정렬

# 양수 케이스
while len(positive_number_list) != 0:        # 리스트의 숫자를 모두 꺼낼 때까지
    if len(positive_number_list) == 1:       # 총 길이가 1이면 마지막 숫자이므로 그냥 더해줌
        result += positive_number_list.pop() 
    else:                                    # 그외는 양수는 오름차에서의 마지막 항이 큰 숫자이므로 
        result += positive_number_list.pop() * positive_number_list.pop() # pop으로 최근 항인 마지막 항부터 꺼내서 곱해서 넣는다.

# 음수 케이스
while len(nagative_number_list) != 0:        # 리스트의 숫자를 모두 꺼낼 때까지
    if len(nagative_number_list) == 1:       # 총 길이가 1이면 마지막 숫자이므로 그냥 더해줌
        result += nagative_number_list.pop()
    else:                                    # 그외는 음수는 내림차순에서의 마지막 항이 큰 숫자이므로 
        result += nagative_number_list.pop() * nagative_number_list.pop()  # pop으로 최근 항인 마지막 항부터 꺼내서 곱해서 넣는다.

print(result)