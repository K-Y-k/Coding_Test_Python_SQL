# 각 카드 종류의 리스트와 중복 여부를 선언해주고
# 각 카드 종류와 몇번 카드인지 슬라이싱으로 가져와서
# 각 카드 리스트에 존재하지 않으면 넣고
# 존재하면 중복이므로 'ERROR' 출력과 중복 여부를 체크해준다.
# 모든 루프를 돌고 난 뒤 중복 여부가 False이면 13장에서 각 카드 리스트의 길이를 뺀 값을 정답에 넣어주고 출력한다.

answer = []
card_li = input()

S_li = []
D_li = []
H_li = []
C_li = []
duplicate = False

for i in range(0, len(card_li), 3):
    if card_li[i] == 'S' and int(card_li[i+1:i+3]) not in S_li:
        S_li.append(int(card_li[i+1:i+3]))
    elif card_li[i] == 'D' and int(card_li[i+1:i+3]) not in D_li:
        D_li.append(int(card_li[i+1:i+3]))
    elif card_li[i] == 'H' and int(card_li[i+1:i+3]) not in H_li:
        H_li.append(int(card_li[i+1:i+3]))
    elif card_li[i] == 'C' and int(card_li[i+1:i+3])not in C_li:
        C_li.append(int(card_li[i+1:i+3]))
    else:
        print('ERROR')
        duplicate = True
        break

if not duplicate:
    answer.append(13 - len(S_li))
    answer.append(13 - len(D_li))
    answer.append(13 - len(H_li))
    answer.append(13 - len(C_li))

    print(' '.join(map(str, answer)))