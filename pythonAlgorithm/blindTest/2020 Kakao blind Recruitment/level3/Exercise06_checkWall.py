def solution(n, weak, dist):
    dist = sorted(dist, reverse=True)
    count = 0
    repair_list = [()]

    for d in dist:
        repair = []
        count += 1

        for idx, point in enumerate(weak):
            start = point
            end_list = weak[idx:] + [n+x for x in weak[:idx]]
            repair.append(set([end % n for end in end_list if end - start <= d]))

        tmp = set()
        for r in repair:
            for rl in repair_list:
                new = r | set(rl)
                #print new
                if len(new) == len(weak):
                    return count
                tmp.add(tuple(new))
        repair_list = tmp
    return -1


print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))
