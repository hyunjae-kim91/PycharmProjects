import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        count = 0 
        x = math.ceil((100-progresses[0])/speeds[0])
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i] * x
        for p in list(progresses):
            if p >= 100:
                progresses.popleft()
                speeds.popleft()
                count += 1
            else:
                break
        answer.append(count)
    print(answer)
    return answer


solution([93,30,55],[1,30,5])
solution([95, 90, 99, 99, 80, 99],[1,1,1,1,1,1])