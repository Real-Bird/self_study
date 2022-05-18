from collections import deque

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    x = input().rstrip()[1:-1].split(",")
    q = deque(x)

    reverse = 0
    flag = 0
    if n == 0:
        q = []

    for i in p:
        if i == "R":
            reverse += 1
        elif i == "D":
            if len(q) < 1:
                flag = 1
                print("error")
                break
            else:
                if reverse % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if flag == 0:
        if reverse % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")