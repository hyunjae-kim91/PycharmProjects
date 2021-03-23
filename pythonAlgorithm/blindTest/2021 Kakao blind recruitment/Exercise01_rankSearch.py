from itertools import combinations as comb
from collections import defaultdict
def solution(info, query):
    answer = []

    # 지원자 경우의 수 계산 (16개) -> 값 오름차순 정렬
    info_dict = defaultdict(list)
    for i in info:
        info_key = i.split()[:-1]
        info_value = int(i.split()[-1])
        for j in range(5):
            for combi in comb(info_key , j):
                key = ''.join(combi)
                info_dict[key].append(info_value)

    dict[key] = []

    print(info_dict)
    for key in info_dict.keys():
        info_dict[key].sort()



    # 쿼리 나눈 후 스코어 판단
    for q in query:
        # 쿼리 나누기
        q = q.split()
        query_key = q[:-1]
        while 'and' in query_key:
            query_key.remove('and')
        while '-' in query_key:
            query_key.remove('-')
        query_key = ''.join(query_key)
        query_value = int(q[-1])

        #lower bound 이용 쿼리 점수보다 높은 개수 찾기
        if query_key in info_dict:
            scores = info_dict[query_key]
            start, end = 0, len(scores)
            while end > start:
                mid = (start + end) // 2
                if scores[mid] >= query_value:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))