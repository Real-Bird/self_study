n = int(input())
plug = 0
for i in range(n):
    plug += int(input())
    if i >= 1:
        plug -= 1

print(plug)