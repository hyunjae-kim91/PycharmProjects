board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

basket = []
answer = 0
for i in moves:
    for j in range(len(board)):
        if board[j][i-1] != 0:
            basket.append(board[j][i-1])
            if len(basket) >= 2:
                if basket[len(basket)-2] == basket[len(basket)-1]:
                    del basket[len(basket)-2]
                    del basket[len(basket)-1]
                    answer += 2
            board[j][i-1] = 0
            break


print(basket)
print(board)
print(answer)
