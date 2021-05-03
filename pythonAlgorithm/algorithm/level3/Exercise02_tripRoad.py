

def solution(tickets):
    route = dict()
    for (start, end) in tickets:
        route[start] = route.get(start, []) + [end]

    for r in route.keys():
        route[r].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if top not in route or len(route[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(route[top][-1])
            route[top] = route[top][:-1]

    return path[::-1]



tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
#result = ["ICN", "JFK", "HND", "IAD"]