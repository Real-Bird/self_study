board = [list(input()) for _ in range(8)]
cnt = 0

for i in range(8):
    for j in range(4):
        if i % 2:
            if board[i][2 * j + 1] == "F":
                cnt += 1
        else:
            if board[i][2*j] == "F":
                cnt += 1

print(cnt)
