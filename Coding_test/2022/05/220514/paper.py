# 종이의 개수

n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]

minus = 0
zero = 0
plus = 0

def clip_paper(x, y, n):
    global minus, zero, plus

    num_check = papers[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (papers[i][j] != num_check):
                for k in range(3):
                    for l in range(3):
                        clip_paper(x + k * n // 3, y + l * n // 3, n // 3)
                return

    if (num_check == -1):
        minus += 1
    elif (num_check == 0):
        zero += 1
    else:
        plus += 1



clip_paper(0, 0, n)
print(f'{minus}\n{zero}\n{plus}')