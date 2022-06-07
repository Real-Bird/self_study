a, b = map(lambda x: int(x, 2), input().split())
print(int(bin(a + b)[2:]))
