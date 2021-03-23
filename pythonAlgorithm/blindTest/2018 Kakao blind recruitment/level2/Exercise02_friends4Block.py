def board2table(m,n,board):
    table = []
    for i in range(n):
        tmp = ''
        for j in range(m):
            tmp += board[j][i]
        table.append(tmp)
    print(table)
    return table

def crash(n,m,table,count=0):
    crash_list = []
    for i in range(n-1):
        for j in range(m-1):
            standard = table[i][j]
            if standard == 'X':
                pass
            elif standard == table[i+1][j] and standard == table[i][j+1] and standard == table[i+1][j+1]:
                crash_list += [(i,j),(i+1,j),(i,j+1),(i+1,j+1)]
    print(crash_list)
    #부서질 블록이 중복인 경우, 삭제
    crash_list = set(crash_list)
    print(crash_list)
    if crash_list:
        for i, j in crash_list:
            table[i] = table[i][:j] + 'X' + table[i][j+1:]

        for i in range(n):
            table[i] = table[i].replace('X','')
            table[i] = 'X' * (m-len(table[i])) + table[i]

        count += len(crash_list)
        return crash(n,m,table,count)

    else:
        return count

def solution(m, n, board):
    table = board2table(m,n,board)
    count = crash(n,m,table)
    return count


print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
#print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

#m,n = 6,6
#board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


