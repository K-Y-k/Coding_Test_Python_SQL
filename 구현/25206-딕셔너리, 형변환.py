# 딕셔너리로 등급과 평점을 넣고
# 입력 받은 학점과 등급을 받아서
# 등급이 P만 아니면 딕셔너리에서 해당 등급의 평점을 받아서
# 학점과 최종 점수를 더해가며 갱신해간다.
# 평균점수는 총 최종 점수를 총 학점으로 나눈 값으로 출력해준다.

credit_total = 0
score_total = 0

grade_dic = {'A+': 4.5, 'A0': 4.0, 
             'B+': 3.5, 'B0': 3.0, 
             'C+': 2.5, 'C0': 2.0, 
             'D+': 1.5, 'D0': 1.0, 
             'F': 0.0}

for _ in range(20):
    subject, credit, grade = map(str, input().split())

    if grade != 'P':
        credit_total += float(credit)
        score_total += float(credit) * grade_dic[grade]

avg = score_total / credit_total

print('{:.6f}'.format(avg))