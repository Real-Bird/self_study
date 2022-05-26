pwd, valid = map(int, input().split())
e = [0 for i in range(1000001)]
result = 0

for i in range(2, 1001):
    if e[i] == 0:
        n = i * 2
        while n < 1000001:
            e[n] = 1
            n += i

for i in range(2, 1000001):
    if e[i] == 0:
        if pwd % i == 0:
            result = i
            break

if result == 0 or result >= valid:
    print("GOOD")
else:
    print("BAD", result)