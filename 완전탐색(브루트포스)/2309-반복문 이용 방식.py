# 9명중에서 7명을 뽑으므로 9C7이므로 9C2와 같다.
# 즉, 9명에서 2명을 뽑는 경우의 수는 9*8 / 2! = 36가지 밖에 안되므로
# 반복문을 사용해도 충분히 시간 복잡도가 느리지 않아서 for문 반복을 활용해서 풀 수 있다.
# 그리고 7명의 키의 총 합은 100cm이므로
# 9명의 총 키 합에서 2명을 뽑은 키를 빼서 100cm일 때 출력하도록 구현할 수 있다.


import sys
smuf_list = []                                              # 난쟁이 리스트 선언

tall_sum = 0                                                # 모든 난쟁이 키 총합 선언 및 초기화
for _ in range(9):                                          # 9명의 난쟁이 키를 리스트에 넣고 키의 총합을 갱신해준다.
    smuf_x = int(sys.stdin.readline().rstrip())
    tall_sum += smuf_x
    smuf_list.append(smuf_x)
    
smuf_list.sort()                                            # 오름차순 정렬

for i in range(9):                                          # 2명을 뽑기 위해 이중 반복문
    for j in range(i+1, 9):
        if tall_sum - smuf_list[i] - smuf_list[j] == 100:   # 9명 키 총합 - 2명을 뽑은 난쟁이 키가 100이면 
            for k in range(9):                              # 현재 2개의 인덱스의 난쟁이 키만 제외해주고 출력하면 된다.
                if k == i or k == j:
                    continue
                else:
                    print(smuf_list[k])
            exit()