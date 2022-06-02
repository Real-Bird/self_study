n = int(input())
repeat = 2 * n
for i in range(1, repeat):
    if i <= n:
        print(("*" * i) + (" " * (repeat - 2 * i)) + ("*" * i))
    else:
        print(("*" * (repeat - i)) + (" " * (repeat - 2 * (repeat - i))) + ("*" * (repeat - i)))
