from itertools import combinations
def solution(relation):
    col = len(relation[0])
    row = len(relation)
    print('col : ' ,col)
    print('row : ' , row)
    #전체 조합
    candidates = []
    for i in range(1,col+1):
        candidates.extend(combinations(range(col),i))

    print('전체 조합 : (열 인덱스)', candidates)

    #유일성
    unique = []
    for c in candidates:
        tmp = [tuple(item[i] for i in c) for item in relation]
        if len(set(tmp)) == row:
            unique.append(c)

    print('유일성 만족 : ' , unique)

    #최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    print('최소성 만족 : ', answer)

    return len(answer)








relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))
# Result = 2 ( 학번, [이름, 전공] )