n = int(input())                            # 입력 값 선언
d = [0] * 1001                              # 문제에서 주어진 n의 범위의 최대 값까지 크기 생성
d[0] = 1                                    # n = 2일 때 2x2인 방법의 수는 2이므로 d[2-1] + d[2-2] = 2로 맞추기 위해 [0]과 [1]을 그에 맞게 초기화한 것
d[1] = 1                                    # n = 1일 때 2x1인 방법의 수는 1이므로

for i in range(2, n + 1):                   # 0과 1은 위에 정의했으므로 2부터 입력한 만큼 bottom-up방식으로 쌓아올림
    d[i] = d[i-1] + d[i-2]   # 점화식
    d[i] %= 10007                           # 문제에서 방법의 수를 100007으로 나눈 나머지라고 했으므로 적용
    
print([n])                                  # 입력 값에 해당하는 방법의 수 출력