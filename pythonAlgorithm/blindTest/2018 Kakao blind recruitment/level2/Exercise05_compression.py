def solution(msg):
    answer = []
    msg_dict = {}
    index = 0
    #A~Z 딕셔너리 추가
    for i in range(26):
        msg_dict[chr(i+65)] = i+1
    new_index = 27

    while index != len(msg):
        a = 1
        while msg[index:index+a] in msg_dict.keys():
            if index + a > len(msg):
                break
            a += 1
        answer.append(msg_dict.get(msg[index:index + a - 1]))
        msg_dict[msg[index:index + a]] = new_index
        new_index += 1
        index = index + a - 1
    return answer

print(solution("KAKAO"))

print(solution("TOBEORNOTTOBEORTOBEORNOT"))

print(solution("ABABABABABABABAB"))

"""
[11, 1, 27, 15]
[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
[1, 2, 27, 29, 28, 31, 30]
"""