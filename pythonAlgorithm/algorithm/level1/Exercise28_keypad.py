#print(key_pad)
#print(key_pad[button.index('*')])
#distance = ((key_pad[4][0] - key_pad[0][0])**2 + (key_pad[4][0] - key_pad[0][0])**2)**0.5

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

def solution(numbers, hand):
    key_pad = []
    button = [1, 4, 7, '*', 2, 5, 8, 0, 3, 6, 9, '#']

    right_coor = [3,2]
    left_coor = [3,0]
    answer = ''

    # 키패드의 좌표 넣기
    for j in range(3):
        for i in range(4):
            key_pad.append([i, j])

    for i in range(len(numbers)):
        if numbers[i] in (1,4,7,'*'):
            answer += 'L'
            left_coor = key_pad[button.index(numbers[i])]
        elif numbers[i] in (3,6,9,'#'):
            answer += 'R'
            right_coor = key_pad[button.index(numbers[i])]
        else:
            right_dist = abs(right_coor[0] - key_pad[button.index(numbers[i])][0]) + abs(right_coor[1]-key_pad[button.index(numbers[i])][1])
            left_dist = abs(left_coor[0] - key_pad[button.index(numbers[i])][0]) + abs(left_coor[1] - key_pad[button.index(numbers[i])][1])
            print("오른쪽 거리 : ",right_dist)
            print("왼쪽 거리 : ",left_dist)
            if right_dist < left_dist:
                answer += 'R'
                right_coor = key_pad[button.index(numbers[i])]
            elif right_dist > left_dist:
                answer += 'L'
                left_coor = key_pad[button.index(numbers[i])]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_coor = key_pad[button.index(numbers[i])]
                else:
                    answer += 'L'
                    left_coor = key_pad[button.index(numbers[i])]

        print(i,"번째 답 : ",answer)
        print("오른쪽 좌표 : ",right_coor)
        print("왼쪽 좌표 : ", left_coor)
        print("-----------------")

    return answer

solution(numbers,hand)
#solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")
#solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right")



"""
입출력 예
numbers	hand	result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"
"""