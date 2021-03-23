from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque()
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for i in cities:
            i = i.upper()
            if i in queue:
                queue.remove(i)
                queue.append(i)
                answer += 1
            elif len(queue) < cacheSize:
                queue.append(i)
                answer += 5
            else:
                queue.popleft()
                queue.append(i)
                answer += 5
            print(queue)
    return answer



cities = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
casheSize = 2
print(solution(casheSize,cities))
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
casheSize = 5
print(solution(casheSize,cities))
