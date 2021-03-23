def solution(msg):
    answer = []
    # A - Z 딕셔너리 만들기
    dict = {}
    for i in range(65, 91):
        dict[chr(i)] = i - 64
    new_value = 27
    # 비교
    idx, i = 0, 0
    while idx + i < len(msg):
        i = 1
        tmp = msg[idx] + msg[idx + i]
        while tmp in dict.keys():
            i += 1
            tmp += msg[idx + i]
        dict[tmp] = new_value
        new_value += 1
        answer.append(dict[msg[idx:idx + i]])
        idx = idx + i
        print('idx', idx)
        print('i', i)
    answer.append(dict[msg[idx:idx+i]])
    print(answer)

    pass

msg = 'KAKAO'
print(solution(msg))