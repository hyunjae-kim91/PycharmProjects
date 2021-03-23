arr = [5,9,7,10]
divisor = 5

#[내 풀이] 더 간단히 표현 -> -1도 나타낼 수 있는 방법...
def solution(arr, divisor):
    answer = sorted([value for i, value in enumerate(arr) if value % divisor == 0])
    if answer == []: answer = [-1]
    print(answer)
    return answer

solution(arr,divisor)


#[내 풀이] 문제 그대로 해석 -> 더 간단하게 나타낼 필요
def solution1(arr, divisor):
    answer = []
    for i, j in enumerate(arr):
        if j % divisor == 0:
            answer.append(j)
    answer.sort()
    if answer == []:
        answer.append(-1)
    print(answer)
    return answer