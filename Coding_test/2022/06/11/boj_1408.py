current = list(map(int, input().split(":")))
start = list(map(int, input().split(":")))
h,m,s = 0, 0, 0
if start[2] - current[2] < 0:
    start[1] -= 1
    start[2] += 60
s += start[2] - current[2]
s %= 60
if start[1] - current[1] < 0:
    start[0] -= 1
    start[1] += 60
m += start[1] - current[1]
m %= 60
if start[0] - current[0] < 0:
    start[0] += 24
h += start[0] - current[0]
h %= 24

print(f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}')
