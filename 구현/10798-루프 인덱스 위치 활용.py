alpha_li = [input() for _ in range(5)]

answer = ''

for i in range(15):
    for j in range(5):
      if i < len(alpha_li[j]):               # 각 열의 길이가 다르므로 인덱스 초과가 발생하지 않게 제약을 두어야 한다.
        answer += alpha_li[j][i]

print(answer)