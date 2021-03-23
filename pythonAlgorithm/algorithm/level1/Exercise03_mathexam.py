answers = [1,2,3,4,5]

# 내가 푼 것
def solution(answers):
    # 수포자 규칙 및 정답 설정
    answer_list = [0 * i for i in range(3)]
    rule1 = [1,2,3,4,5]
    rule2 = [2,1,2,3,2,4,2,5]
    rule3 = [3,3,1,1,2,2,4,4,5,5]

    # 정답 길이에 맞춰 최소한의 리스트 설정
    list1 = [i for i in rule1 * (len(answers) // len(rule1) + 1)]
    list2 = [i for i in rule2 * (len(answers) // len(rule2) + 1)]
    list3 = [i for i in rule3 * (len(answers) // len(rule3) + 1)]

    #정답 비교
    for i in range(len(answers)):
        if answers[i] == list1[i]:
            answer_list[0] += 1
        if answers[i] == list2[i]:
            answer_list[1] += 1
        if answers[i] == list3[i]:
            answer_list[2] += 1

    #최대값 확인 후, 인덱스 전부 반환
    answer = [i + 1 for i, value in enumerate(answer_list) if value == max(answer_list)]
    print(answer)
    return answer

#enumerate 제대로 이용하기 / 다른 사람 답안
#enumerate : list의 index, value을 반환 / 인덱스 번호와 컬렉션 원소를 tuple로 반환
def solution1(answers):

    # 정답 패턴 한 이중 리스트, 정답 개수 리스트 선언
    student = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    answer = [0] * len(student)

    # student 리스트의 index는 i , value는 j
    for i , j in enumerate(answers):
        for k, l in enumerate(student):
            if j == l[i % len(l)]:
                answer[k] += 1

    print([i + 1 for i, value in enumerate(answer) if value == max(answer)])

    return [i + 1 for i, value in enumerate(answer) if value == max(answer)]


solution1(answers)
