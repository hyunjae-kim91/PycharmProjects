def change_code(music):
    music = music.replace('C#', 'c')
    music = music.replace('D#', 'd')
    music = music.replace('F#', 'f')
    music = music.replace('G#', 'g')
    music = music.replace('A#', 'a')
    return music
def solution(m, musicinfos):
    # 음악 시간 구하기
    answer_list = []
    m = change_code(m)
    idx = 1
    for i in range(len(musicinfos)):
        music = musicinfos[i].split(',')
        music[3] = change_code(music[3])
        time = (int(music[1].split(':')[0]) - int(music[0].split(':')[0])) * 60 + int(music[1].split(':')[1]) - int(music[0].split(':')[1])
    # 재생 시간 동안 전체 악보정보
        length = len(music[3])
        music[3] = music[3]*(time//length) + music[3][:time%length]
        print(music)
    # 제목 반환 -> 없을 땐 none / 여러 개 일 때는 재생 시간이 가장 긴 것 선택 (재생 시간 같으면 앞 쪽 재생 제목 선택)
        if m in music[3]:
            answer_list.append([idx, time, music[2]])
        idx += 1
    answer_list = sorted(answer_list, key = lambda x: (-x[1],x[0]) )
    print(answer_list)
    if answer_list:
        return answer_list[0][2]
    else:
        return "(None)"

"""
m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m,musicinfos))
"""
m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B","03:00,03:31,FO1,CC#B","04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m,musicinfos))

"""
m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m,musicinfos))
"""