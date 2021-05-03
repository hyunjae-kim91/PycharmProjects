from collections import deque
def solution(n, computers):
    network = 0
    queue = deque()
    visit = [False for _ in range(n)]

    for i in visit:
        if not i:
            while queue:
                for idx, i in enumerate(queue[0]):
                    if (not visit[idx]) and i == 1:
                        queue.append(computers[idx])
                        visit[idx] = True
        network += 1










    pass


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))