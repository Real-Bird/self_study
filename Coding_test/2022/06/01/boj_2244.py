n = int(input())
x = n * 2 - 1
for i in range(x):
    if i < n:
        print(f"{(' ' * (n - i - 1))}{('*' * (2 * i + 1))}")
    else:
        print(f"{(' ' * (i - n + 1))}{('*' * (2 * (x - i - 1) + 1))}")
