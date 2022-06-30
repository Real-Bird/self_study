n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
a.sort()
b.sort(reverse=True)

for i, j in zip(a, b):
    s += i * j

print(s)