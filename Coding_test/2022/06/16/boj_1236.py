n, m = map(int, input().split())
castle = [input() for _ in range(n)]
row = 0
col = 0
for i in range(n):
    if "X" not in castle[i]:
        row += 1

for i in range(m):
    if "X" not in [castle[j][i] for j in range(n)]:
        col += 1

print(max(row, col))