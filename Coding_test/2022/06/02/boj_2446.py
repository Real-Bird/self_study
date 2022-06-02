n = int(input())
repeat = n * 2
for i in range(1, repeat):
    if i <= n:
        print((" " * (i - 1)) + ("*" * (repeat - (2 * i - 1))))
    else:
        print((" " * (repeat - i - 1)) + ("*" * (repeat - (2 * (repeat - i) - 1))))
