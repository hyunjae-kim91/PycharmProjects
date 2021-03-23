def insert(m,a,b,key,board):
    for i in range(m):
        for j in range(m):
            board[i+a][j+b] += key[i][j]
    return board

def delete(m,a,b,key,board):
    for i in range(m):
        for j in range(m):
            board[i+a][j+b] -= key[i][j]
    return board

def check(m,n,board):
    board = [i[m:m+n] for i in board[m:m+n]]
    for i in board:
        for j in i:
            if j != 1:
                return False
    return True

def rotate(board):
    return list(zip(*board[::-1])) # [::-1] -> 역순 / zip() 요소 합치기 / *iterable -> 여러 개의 iterable로 다시 나누기(unpack)

def solution(key, lock):
    m, n = len(key), len(lock)
    ext_lock = [[0 for _ in range(2*m+n)] for _ in range(2*m+n)]  # 자물쇠와 키 합친 크기만큼 큰 빈 공간 생성
    for i in range(n):     # 자물쇠 번호 입력
        for j in range(n):
            ext_lock[i+m][j+m] = lock[i][j]

    rot_key = key
    for _ in range(4):
        for a in range(1,m+n):
            for b in range(1,m+n):
                board = insert(m,a,b,rot_key,ext_lock)
                if check(m,n,board):
                    return True
                board = delete(m,a,b,rot_key,ext_lock)
        rot_key = rotate(rot_key)
    return False


key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

print(solution(key,lock))
