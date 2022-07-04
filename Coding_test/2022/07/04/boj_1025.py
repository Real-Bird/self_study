n, m = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(input()))

result = -1

for i in range(n):
    for j in range(m):
        for weight_n in range(-n, n):
            for weight_m in range(-m, m):
                if weight_n == 0 and weight_m == 0:
                    continue
                step = 0
                x = i
                y = j
                value = ""
                while (0 <= x < n) and (0 <= y < m):
                    value += table[x][y]
                    step += 1
                    value_int = int(value)
                    value_sqrt = value_int ** 0.5
                    value_decimal = value_sqrt - int(value_sqrt)
                    if value_decimal == 0 and value_int > result:
                        result = value_int
                    x = i + step * int(weight_n)
                    y = j + step * int(weight_m)

print(result)