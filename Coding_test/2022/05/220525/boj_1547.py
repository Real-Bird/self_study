m = int(input())
cups = [1, 2, 3]
for i in range(m):
    x, y = map(int, input().split())
    idx = cups.index(x)
    idy = cups.index(y)
    cups[idx] = y
    cups[idy] = x

print(cups[0])