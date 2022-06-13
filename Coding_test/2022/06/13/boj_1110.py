n = input().rstrip().zfill(2)
tmp = n[1] + str(sum(map(int, n))).zfill(2)[1]
cnt = 1

while int(n) != int(tmp):
    tmp = tmp[1] + str(sum(map(int, tmp))).zfill(2)[1]
    cnt += 1

print(cnt)
