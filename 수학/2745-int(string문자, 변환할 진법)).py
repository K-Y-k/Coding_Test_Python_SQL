N, B = map(str, input().split())

N_B = int(N, int(B))              # 위 입력한 문자 N을 B진법으로 변환
 
print(int(N_B))                   # N진법을 10진법으로 다시변환해서 출력 (10진법 변환은 그냥 int()임)