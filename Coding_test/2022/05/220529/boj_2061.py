k, l = map(int, input().split())

for i in range(2, l):
    if not (k % i):
        print("BAD", i)
        exit()

print("GOOD")