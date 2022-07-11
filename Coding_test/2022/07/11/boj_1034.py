n, m = map(int, input().split())
table = []

for _ in range(n):
    table.append(list(map(int, list(input()))))

k = int(input())
max_cnt = 0

for i in range(n):
    cnt_0 = 0
    for j in table[i]:
        if j == 0:
            cnt_0 += 1

    row_cnt = 0
    if cnt_0 <= k and cnt_0 % 2 == k % 2:
        for h in range(n):
            if table[i] == table[h]:
                row_cnt += 1

    max_cnt = max(max_cnt, row_cnt)

print(max_cnt)