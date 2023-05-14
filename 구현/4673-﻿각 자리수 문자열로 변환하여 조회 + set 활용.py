# 1~10000을 range 범위로 하여 모두 적용한 리스트를 만들고
# 모두 조회해서 각 자리수를 더한 것은 결국 생성자이기에 셀프 숫자로 올 수 없어
# 생성자 리스트에 넣고 모두 조회된 후의 생성자 리스트를 모두 조회해서
# 위 1~10000범위의 리스트에 속해있으면 지워주어 셀프 숫자만 있게 만들고 출력한다.

# 생성자가 중복으로 올 수 있는데 이 문제에서는 중복이어도 잘 작동되지만
# set()으로 감싸고 루프 조회하면 중복된 것을 모두 지우고 조회가능하여 속도가 좀 더 빨라진다.


num_list = list(range(1, 10001))         # 문제에서 원하는 범위만큼 적용한 리스트
constructor_list = []                    # 생성자 리스트 선언

for i in num_list:                       # 1~10000모든 숫자 조회
    for j in str(i):                     # 각 자리수로 쪼개기 위해 str()로 문자열로 만들어서 조회
        i += int(j)                      # 각 자리수를 더하고
    if i <= 10000:                       # 각 자리수를 모두 더한 것은 생성자로 10000이하이면
        constructor_list.append(i)       # 생성자 리스트에 추가한다.
        
for i in set(constructor_list):          # set()으로 감싸고 조회하면 중복은 제거된 상태로 조회
    if i in num_list:                    # 1~10000의 리스트에 있으면
        num_list.remove(i)               # 지워주어 셀프 숫자로만 있게 만들기

for i in num_list:                       # 위 작업으로 셀프 숫자만 남은 것을 조회하며 출력하기
    print(i)