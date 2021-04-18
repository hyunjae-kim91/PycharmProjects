from collections import Counter


def solution(a, edges):
    for edge in edges:
        if edges == 0:
            bool = True
        else:
            bool = False
            break
    if bool:
        return 0
    if sum(a):
        return -1

    dict = Counter()
    tmp = []
    for edge in edges:
        for j in edge:
            tmp.append(j)
    dict = Counter(tmp)

    for j in range(len(a)):
        if j not in dict.keys() and a[j] != 0:
            return -1
    count = 0

    edges = sorted(edges, key = lambda x: min(dict[x[0]],dict[x[1]]))

    for edge in edges:
        i, j= edge
        if dict[i] >= dict[j]:
            a[i] += a[j]
            count += abs(a[j])
            a[j] = 0
        else:
            a[j] += a[i]
            count += abs(a[i])
            a[i] = 0
        print(a)
    if a != [0]*len(a):
        return -1
    return count



a = [-5, 0, 2, 1, 2]
edges = [[0, 1], [3, 4], [0, 3], [2, 3]]

print(solution(a, edges))

"""
각 점에 가중치가 부여된 트리가 주어집니다. 당신은 다음 연산을 통하여, 이 트리의 모든 점들의 가중치를 0으로 만들고자 합니다.
임의의 연결된 두 점을 골라서 한쪽은 1 증가시키고, 다른 한쪽은 1 감소시킵니다.
하지만, 모든 트리가 위의 행동을 통하여 모든 점들의 가중치를 0으로 만들 수 있는 것은 아닙니다. 당신은 주어진 트리에 대해서 해당 사항이 가능한지 판별하고, 만약 가능하다면 최소한의 행동을 통하여 모든 점들의 가중치를 0으로 만들고자 합니다.
트리의 각 점의 가중치를 의미하는 1차원 정수 배열 a와 트리의 간선 정보를 의미하는 edges가 매개변수로 주어집니다. 주어진 행동을 통해 트리의 모든 점들의 가중치를 0으로 만드는 것이 불가능하다면 -1을, 가능하다면 최소 몇 번만에 가능한지를 찾아 return 하도록 solution 함수를 완성해주세요. (만약 처음부터 트리의 모든 정점의 가중치가 0이라면, 0을 return 해야 합니다.)
제한사항
a의 길이는 2 이상 300,000 이하입니다.
a의 모든 수는 각각 -1,000,000 이상 1,000,000 이하입니다.
a[i]는 i번 정점의 가중치를 의미합니다.
edges의 행의 개수는 (a의 길이 - 1)입니다.
edges의 각 행은 [u, v] 2개의 정수로 이루어져 있으며, 이는 u번 정점과 v번 정점이 간선으로 연결되어 있음을 의미합니다.
edges가 나타내는 그래프는 항상 트리로 주어집니다.
입출력 예
a	edges	result
[-5,0,2,1,2]	[[0,1],[3,4],[2,3],[0,3]]	9
[0,1,0]	[[0,1],[1,2]]	-1
입출력 예 설명
입출력 예 #1
다음 그림은 주어진 트리의 모든 정점의 가중치를 0으로 만드는 과정을 나타낸 것입니다.
all_zero_example.png
2번 정점과 3번 정점을 선택하여 2번 정점은 1 감소시키고, 3번 정점은 1 증가시킵니다. (2번 반복)
3번 정점과 4번 정점을 선택하여 4번 정점은 1 감소시키고, 3번 정점은 1 증가시킵니다. (2번 반복)
0번 정점과 3번 정점을 선택하여 3번 정점은 1 감소시키고, 0번 정점은 1 증가시킵니다. (5번 반복)
모든 정점의 가중치를 0으로 만드는 데 필요한 최소 행동 횟수는 9번이므로, 9를 return 해야 합니다.
입출력 예 #2
주어진 트리는 모든 정점의 가중치를 0으로 만드는 것이 불가능하므로, -1을 return 해야 합니다.
"""
