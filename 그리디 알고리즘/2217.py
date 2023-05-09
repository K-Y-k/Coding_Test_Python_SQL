# 예를 들어 로프의 주어진 중량보다 크고 만약 또 다른 로프가 있을 시 나누기 2를 한 값이 최대 중량이 되는 원리이다.

# 즉, 각 로프의 개수에 따른 최대 중량을 구하려면 
# (입력한 로프 값 중 제일 큰 중량) x (로프의 개수)가  각 로프 개수에 따른 최대 값이다.

# 그러므로 입력한 로프 중량을 오름차순으로 정렬하고 (각 로프 중량) x (로프 개수)를 한 값을 결과 배열에 넣고
# 결과 배열 안의 가장 큰원소 값이 최대 중량이다. 



N = int(input())   		               # 로프 입력 개수 선언
rope_list = list()  		           # 로프 리스트 선언
result = []                            # 결과 배열 초기화

for _ in range(N) :                    # 입력 개수 만큼 로프 중량 입력하고 로프 리스트에 추가
    rope_list.append(int(input()))

rope_list.sort(reverse=True)  	       # 오름차순으로 정렬

for i in range(N) :		               # 각 원소 * 로프 개수
    result.append(rope_list[i] * (i+1))

print(max(result))  		           # 제일 큰 값 출력