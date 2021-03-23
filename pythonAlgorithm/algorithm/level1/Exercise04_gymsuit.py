n = 5
lost = [2,4]
reserve = [3]

def solution(n, lost, reserve):
    answer = 0
    # 전체 학생 선언 후, 여분 가져온 사람 + 1 / 잃어버린 사람 - 1
    student = [1] * n
    for i in reserve:
        student[i - 1] += 1
    for j in lost:
        student[j - 1] -= 1

    for i, j in enumerate(student):
        print(i, j)
        if j == 0:
            if i == 0 and student[i + 1] == 2:
                student[i + 1] -= 1
                student[i] += 1
            elif i == len(student) - 1 and student[i - 1] == 2:
                student[i - 1] -= 1
                student[i] += 1
            elif i != 0 and i != len(student) - 1:
                if student[i - 1] == 2 or student[i + 1] == 2:
                    if student[i - 1] != 2 and student[i + 1] == 2:
                        student[i + 1] -= 1
                        student[i] += 1
                    else:
                        student[i - 1] -= 1
                        student[i] += 1

    answer = n - student.count(0)
    print(answer)
    return answer

solution(n, lost, reserve)
