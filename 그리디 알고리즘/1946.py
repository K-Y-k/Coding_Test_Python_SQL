import  sys                                      # stdin.readline()을 사용하기 위해  선언 -> 반복문에서 여러 줄을 입력할 때 효율적 시간초과 방지

for _ in range(int(sys.stdin.readline())) :     # 첫 번째 줄 = 입력한 만큼 실행
    people_list = []                            # 각 성적을 담을 리스트 선언

    for j in range(int(sys.stdin.readline())) :  # 입력한 만큼의 사원 성적 입력
        people_list.append(list(map(int, sys.stdin.readline().split())))  # 공백을 기준으로  2차원 리스트 담기
    
    people_list.sort()                           # 1차원 배열 낮은 순으로 정렬
    temp = people_list[0][1]                     # 서류면접 제일 높은 등수를 첫 기준 값 담기
    count = 1                                    # 합격자 수 변수 선언

    for j in range(len(people_list)) :           # 리스트 길이 만큼 반복
                                                 # 가장 최근에 합격처리가 된 사람보다 면접을 잘 본 사람을 찾아야 한다.
        if temp > people_list[j][1] :            # 기준 값 보다 면접을 잘 본 사람이 나왔을 때
            count += 1                           # 합격 처리
            temp = people_list[j][1]             # 합격 기준을 방금 합격한 사람 등수로 변경

    print(count)                                 # 합격자 수 출력