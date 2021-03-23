def possible(answer):
    for x, y, a in answer:
        if a == 0:
            if y != 0 and (x,y,1) not in answer and (x-1,y,1) not in answer and (x,y-1,0) not in answer:
                return True
        else:
            if (x,y-1,0) not in answer and (x+1,y-1,0) not in answer and not ((x-1,y,1) in answer and (x+1,y,1) in answer):
                return True
    return False

# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

def solution(n, build_frame):
    answer = set()
    for build in build_frame:
        x, y, a, b = build[0], build[1], build[2], build[3]
        b_set = (x,y,a)
        if b:
            answer.add(b_set)
            if possible(answer):
                answer.remove(b_set)
        elif b_set in answer:
            answer.remove(b_set)
            if possible(answer):
                answer.add(b_set)
    answer = map(list, answer)
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


# a=0 -> 기둥 /a=1 -> 보
# b=0 -> 삭제 / b=1 -> 설치

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
