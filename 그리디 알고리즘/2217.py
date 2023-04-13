N = int(input())   		           # 로프 입력 개수 선언
rope_list = list()  		       # 로프 리스트 선언
result = []                        # 결과 배열 초기화

for _ in range(N) :                # 입력 개수 만큼 로프 중량 입력하고 로프 리스트에 추가
    rope_list.append(int(input()))

rope_list.sort(reverse=True)  	   # 오름차순으로 정렬

for i in range(N) :		           # 각 원소 * 로프 개수
    result.append(rope_list[i] * (i+1))

print(max(result))  		       # 제일 큰 값 출력