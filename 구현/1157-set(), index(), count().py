# 내가 푼 방식
# 입력 받은 문자를 대문자로 만들고
# 딕셔너리를 만들어서 각 단어의 횟수를 반영하고
# 딕셔너리를 값 기준 내림차순으로 정렬한 후
# 딕셔너리를 조회해서 최대 값이면 최대값과 최대 값의 문자를 갱신하고 정답 리스트에 추가하여
# 정답 리스트가 2개 이상이면 ?로 출력하게 했다.

s = str(input())
s = s.upper()

alpha_dic = {}

for i in s:
    if i not in alpha_dic:
        alpha_dic[i] = 1
    else:
        alpha_dic[i] += 1


alpha_dic = sorted(alpha_dic.items(), key=lambda x:x[1], reverse=True)

tmp_max = 0
tmp_str = ''
answer_li = []

for key, val in alpha_dic:
    if val > tmp_max:
        tmp_max = val
        tmp_str = key
        answer_li.append(key)
    elif val == tmp_max:
        answer_li.append(key)


if len(answer_li) > 1:
    print('?')
else:
    print(tmp_str)



# 원래 입력한 단어와 중복을 제거한 단어를 나눈 후
# set(), count(), index()를 활용한 방식

origin_s = input().upper()                     # 대문자를 씌우고
set_s = list(set(origin_s))                    # 입력받은 문자열에서 중복값을 제거

count_li = []                                  # 카운팅 한 숫자 리스트


for i in set_s:
    count = origin_s.count(i)                  # 원본에서의 카운팅을 한 후
    count_li.append(count)                     # 카운팅 한 숫자를 리스트에 넣고


if count_li.count(max(count_li)) > 1:          # count 숫자 최대값이 중복되면
    print('?')                                 # ? 출력
else:
    max_index = count_li.index(max(count_li))  # count 숫자 최대값의 인덱스(위치)로 가져와서
    print(set_s[max_index])                    # count 리스트와 중복값을 제거한 단어의 인덱스가 일치하므로 중복값을 제거한 단어의 인덱스 값으로 출력