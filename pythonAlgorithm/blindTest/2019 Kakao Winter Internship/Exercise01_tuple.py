import re
def solution(s):
    answer = []
    p = sorted(re.findall('{[\d,]+}', s), key=lambda x: len(x))

    for i in p:
        a = i[1:len(i) - 1].split(",")
        for i in a:
            if int(i) not in answer:
                answer.append(int(i))

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
#s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
s = "{{20,111},{111}}"

print(solution(s))




import re
from collections import Counter

def solution(s):

    s = Counter(re.findall('\d+', s))
    print(s)
    print([int(k) for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)])
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
#s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
#s = "{{20,111},{111}}"

print(solution(s))
