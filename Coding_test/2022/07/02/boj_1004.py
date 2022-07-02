t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())
        d1 = (((x1 - cx) ** 2) + ((y1 - cy) ** 2)) ** 0.5
        d2 = (((x2 - cx) ** 2) + ((y2 - cy) ** 2)) ** 0.5
        if (d1 < r < d2) or (d1 > r > d2):
            cnt += 1
    print(cnt)
