# 내가 푼 방식
# 비교할 기준의 초깃값을 시간, 곡이름으로 두었고
# #이 붙은 음표는 이어붙이면 구분이 안가서 소문자로 모두 변경해주고
# 시간을 분단위로 만들어준 후 시작시간, 끝난시간, 곡이름, 음표를 쪼개서
# 시작시간 - 끝난시간으로 그 시간만큼의 음표를 이어붙였다.
# 시간이 비교할 기준의 시간보다 길고 문제에서 원하는 음표가 포함되어 있으면 최신화 해준다.

# 부족했던점 : 이어붙인 후에 #이 붙은 것을 replace작업을 하였지만 이는 음표가 1400개나 주어지면 시간초과가 발생할 수 밖에 없다.
#              처음 쪼갰을 때 변환해줘야한다.

def solution(m, musicinfos):
    answer = {'time': 0, 'name': '(None)'}     # 비교할 기준의 초깃값을 시간, 곡이름으로 두었고

    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#','g').replace('A#', 'a') # #이 붙은 음표는 이어붙이면 구분이 안가서 소문자로 모두 변경해주고

    for i in musicinfos:
        start, end, name, code = i.split(',')  # 시작시간, 끝난시간, 곡이름, 음표를 쪼개서

        # 부족했던점 : 이어붙인 후에 #이 붙은 것을 replace작업을 하였지만 이는 음표가 1400개나 주어지면 시간초과가 발생할 수 밖에 없다.
        #              처음 쪼갰을 때 변환해줘야한다.
        code = code.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a') 

        # 시간을 분단위로 만들어준 후 
        start_hour, start_minuate  = start.split(':')
        start_value = int(start_hour) * 60 + int(start_minuate)

        end_hour, end_minuate  = end.split(':')
        end_value = int(end_hour) * 60 + int(end_minuate)

        time = end_value - start_value         # 시작시간 - 끝난시간으로

        if time > len(code):                   # 그 시간만큼의 음표를 이어붙였다.
            if time % len(code) == 0:
                code_a = code * (time // len(code))
            else:
                code_a = code * (time // len(code)) + code[:time % len(code) + 1]
        else:
            code_a = code[:time]


        if m in code_a and time > answer['time']: # 시간이 비교할 기준의 시간보다 길고 문제에서 원하는 음표가 포함되어 있으면
            answer['time'] = time                 # 최신화 해준다.
            answer['name'] = name 


    return answer['name']