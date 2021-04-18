from collections import deque
def move(s1, s2, n_board):
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    cand = []
    for dy,dx in move:
    # 1. 상,하,좌,우 이동
    # 이동 후, 둘 다 0이면 큐에 추가
        if n_board[s1[0]+dy][s1[1]+dx] == 0 and n_board[s2[0]+dy][s2[1]+dx] == 0:
            cand.append(((s1[0]+dy,s1[1]+dx),(s2[0]+dy,s2[1]+dx)))
    #2. 가로 일 때, 세로로 회전
    if s1[1] == s2[1]:
        for d in [-1,1]:
            if n_board[s1[0]][s1[1]+d] == 0 and n_board[s2[0]][s2[1]+d] == 0:
                cand.append((s1,(s1[0],s1[1]+d)))
                cand.append((s2,(s2[0],s2[1]+d)))
    #3. 세로 일 때, 가로로 회전
    else:
        for d in [-1,1]:
            if n_board[s1[0]+d][s1[1]] == 0 and n_board[s2[0]+d][s2[1]] == 0:
                cand.append(((s1[0]+d, s1[1]), s1))
                cand.append(((s2[0]+d, s2[1]), s2))

    return cand


def solution(board):
    n = len(board)
    print(n)
    n_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            n_board[i+1][j+1] = board[i][j]
    # [0] : 열 / [1] : 행
    queue = deque([((1,1),(2,1),0)])
    conf = set([((1,1),(2,1))])
    while queue:
        s1, s2, count = queue.popleft()
        if s1 == (n,n) or s2 == (n,n):
            return count
        for cand in move(s1,s2,n_board):
            if cand not in conf:
                queue.append((*cand,count+1))
                conf.add(cand)

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# Result= 7

print(solution(board))