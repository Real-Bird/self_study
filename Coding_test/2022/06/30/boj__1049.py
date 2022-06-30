n, m = map(int, input().split())
packages = []
eachs = []
answer = 0
for _ in range(m):
    package, each = map(int, input().split())
    packages.append(package)
    eachs.append(each)

packages.sort()
eachs.sort()

if packages[0] <= eachs[0] * 6:
    answer = (n // 6) * packages[0] + (n % 6) * eachs[0]
    if packages[0] < (n % 6) * eachs[0]:
        answer = packages[0] * ((n//6) + 1)
else:
    answer = n * eachs[0]

print(answer)