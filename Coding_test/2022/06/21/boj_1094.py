x = int(input())
sticks = [64]
remain = 0
while True:
    remain = sum(sticks)
    if remain == x:
        break
    tmp = sticks.pop() // 2
    sticks.append(tmp)
    if sum(sticks) < x:
        sticks.append(tmp)

print(len(sticks))