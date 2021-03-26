from collections import deque
def move(s_1, s_2, count):
    #1. 상,하,좌,우 이동
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    for m in move:
        
        pass

    #2. 가로 일 때, 세로로 회전
    if s_1[1] == s_2[1]:
        pass

    #3. 세로 일 때, 가로로 회전
    if s_1[0] == s_2[0]:
        pass


    return s_1, s_2, count


def solution(board):
    col, row = len(board), len(board[0])
    n_board = [[0] * (row+2) for _ in range(col+2)]
    for i in range(col):
        for j in range(row):
            n_board[i+1][j+1] = board[i][j]
    print(n_board)

    queue = deque([[(1,1),(2,1),0]])
    pop = queue.popleft()
    s_1, s_2, count = pop[0], pop[1], pop[2]
    print(pop, s_1, s_2, count)
    move(s_1,s_2)


    pass


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# Result= 7

print(solution(board))