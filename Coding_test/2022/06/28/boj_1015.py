n = int(input())
a = list(map(int, input().split()))
p = []
tmp = a.copy()
tmp.sort()

for i in a:
    p.append(tmp.index(i))
    tmp[tmp.index(i)] = -1

print(*p)