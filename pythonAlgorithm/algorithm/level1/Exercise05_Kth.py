array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

#내가 푼 것
def solution(array,commands):
    answer = []
    for i in commands:
        #배열 슬라이싱 후 정렬
        array_temp =  sorted(array[i[0]-1:i[1]])
        #정답에 추가
        answer.append(array_temp[i[2]-1])
        print(answer)

#map, lambda 배우기
#map 리스트나 튜블의 요소를 지정 함수로 처리, (함수, 리스트) / map을 그냥 print하면 map 객체만 보여줘서 판단 불가
#Ex. list(map(int, a)) / list(map(str, range(10))
#lambda함수는 익명 함수로 임시적으로 쓰는 함수
#Ex. square = lambda x : x**2 / print(square(7)) --> 49
#map하고 lambda하고 같이 쓰면 -->  list(map(lambda x : x**2, range(5)) --> [0,1,4,9,16]

def solution1(array , commands):
    print(list(map(lambda x : sorted(array[x[0]-1:x[1]])[x[2]-1],commands)))

solution(array,commands)