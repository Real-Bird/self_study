def is_ujin(a, b):
    x, y = 1, 1
    for i in a:
        x *= int(i)
    for j in b:
        y *= int(j)
    return True if x == y else False


n = input().rstrip()

flag = False

for i in range(1, len(n)):
    forward = n[:i]
    backward = n[i:]
    if is_ujin(forward, backward):
        flag = True

if flag:
    print("YES")
else:
    print("NO")
