from itertools import combinations
def solution(orders, course):
    answer = []
    # orders(주문) 알파벳 오름차순으로 정렬
    orders = [sorted(i) for i in orders]

    # 주문 길이가 코스 길이보다 크면 코스 리스트에서 제외 ex. orders = ['AB','BC'] / course = [2,3,4] --> course에서 3,4 제외
    maximum = max([len(i) for i in orders])
    course = [i for i in course if i <= maximum]

    #2개부터 딕셔너리에 추가
    for i in course:
        dictionary = {}
        for j in orders:
            b = list(map(list,combinations(j,i)))
            for k in b:
                join_str = ""
                for l in k:
                    join_str += l
                if dictionary.get(join_str) != None:
                    dictionary[join_str] += 1
                else:
                    dictionary[join_str] = 1
        dictionary_max = max(dictionary.values())
        if dictionary_max > 1:
            for i in dictionary.keys():
                if dictionary[i] == dictionary_max:
                    answer.append(i)
        answer.sort()
    return answer







#print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
#Result = ["AC", "ACDE", "BCFG", "CDE"]
#print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
#Result = ["ACD", "AD", "ADE", "CD", "XYZ"]
#print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
#Result = ["WX", "XY"]

from itertools import combinations
import collections

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)
        most_ordered = collections.Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return [ ''.join(v) for v in sorted(result) ]


print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

