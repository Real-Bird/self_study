s = int(input())
l = list(map(int, input().split()))
l.append(0)
l.sort()
n = int(input())
tmp = 0
for i in range(s):
    if l[i] == n or l[i+1] == n:
        tmp = 0
        break
    elif l[i] < n < l[i+1]:
        tmp = (n - l[i]) * (l[i+1] - n) - 1
        break

print(tmp)