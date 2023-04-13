import sys

def GCD(n, m) :                                              # 최대 공약수 구하는 (유클리드 호제) 함수
    if m == 0 :                                              # 0이 되었을 때의 값이 최대 공약수이므로 0이 될 때까지 나눈다.
        return n
    else :
        return GCD(m, n%m)

N = int(input())                                             # 입력 값 선언

for _ in range(N) :                                          # 입력 값만큼 반복
    sum = 0                                                  # 합 변수 초기화
    A_list = []                                              # 리스트 초기화 
    A_list = list(map(int, sys.stdin.readline().split()))    # 입력 값 선언


    for i in range(1, A_list[0]) :                           # 문제에서 첫번째 항 A_list[0]이 입력한 개수이고 
                                                             # 이중 for문에서 끝까지 비교하므로 A_list[0]+1만큼이 아닌 A_list[0]으로 마지막 항은 제외해준 것이다.
        for j in range(i+1, A_list[0]+1) :                   # 이중 for문으로 위 i가 두번째 항(최대공약수를 구해야할 첫 번째 값)으로
                                                             # 다음 대상인 j는 i+1부터 끝까지인 A_list[0]+1까지 반복
            G = GCD(A_list[i], A_list[j])                    # 최대공약수 계산
            sum += G                                         # 합산 적용

    print(sum)                                               # 결과 출력