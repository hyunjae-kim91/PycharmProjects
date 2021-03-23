def solution(record):
    act = []
    name = {}

    # id와 이름 분리 후, dictionary 추가
    for i in record:
        if len(i.split(' ')) == 3:
            name[i.split(' ')[1]] = i.split(' ')[2]
        act.append([i.split(' ')[0], i.split(' ')[1]])

    # 딕셔너리 사전 내 이름 바꾸기
    for i in act:
        i[1] = name.get(i[1])

    # 한글 변환 딕셔너리
    translate = {'Enter' : "님이 들어왔습니다.", 'Leave' : "님이 나갔습니다."}

    return [i[1] + str(translate.get(i[0])) for i in act if translate.get(i[0])]


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
#Result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


