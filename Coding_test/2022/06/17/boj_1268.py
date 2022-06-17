n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]
same_same = [[0] * n for _ in range(n)]

for i in range(5):
    for j in range(n):
        for k in range(j + 1, n):
            if classes[j][i] == classes[k][i]:
                same_same[k][j] = 1
                same_same[j][k] = 1

cnt = []
for same in same_same:
    cnt.append(same.count(1))

print(cnt.index(max(cnt)) + 1)
