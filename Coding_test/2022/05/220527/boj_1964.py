n = int(input())
five = 5
point = 7
for i in range(1, n):
    five += point
    point += 3

print(five % 45678)