def solution(lines):
    time_list = []
    interval_list = []
    # 1. 날짜 / 시간 / 처리 시간 나누기
    for a in lines:
        tmp = a.split(' ')
        time_tmp = tmp[1].split(':')
        time = float(time_tmp[0]) * 3600 + float(time_tmp[1]) * 60 + float(time_tmp[2])
        op_time = float(tmp[2][:-1]) - 0.001
        interval = [time - op_time, time]
        time_list.append(interval)

    # 2. 종료 값 기준 sorting
    time_list = sorted(time_list, key = lambda x : x[1])
    print(time_list)
    answer = 0
    for i in range(len(time_list)):
        a = 1
        for j in range(i+1, len(time_list)):
            if time_list[i][1] + 1 >= time_list[j][0]:
                a += 1
        if a > answer:
            answer = a
    return answer



    #line_tmp = [[a.split(' ')[1],a.split(' ')[2]] for a in lines]
    #print(line_tmp)
    pass




lines = ["2016-09-15 20:59:57.421 0.351s","2016-09-15 20:59:58.233 1.181s","2016-09-15 20:59:58.299 0.8s","2016-09-15 20:59:58.688 1.041s","2016-09-15 20:59:59.591 1.412s","2016-09-15 21:00:00.464 1.466s","2016-09-15 21:00:00.741 1.581s","2016-09-15 21:00:00.748 2.31s","2016-09-15 21:00:00.966 0.381s","2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))

"""
입력: [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

출력: 7
"""