def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,(len(arr))):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
    print(answer)


def solution1(arr):

    answer = [value for a, value in enumerate(arr) if arr[a] != arr[a+1]]
    print(answer)

array = [1,1,3,3,0,1,1]
array_1 = [4,4,4,3,3]
solution1(array)