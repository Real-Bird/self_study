c, n = map(int, input().split())
cost_list = []
for _ in range(n):
    cost_list.append(tuple(map(int, input().split())))
cost_list.sort()

dp = [0] + [1000000] * (c + 100)
min_invest = int(1e9)

for cost, visitor in cost_list:
    for i in range(visitor, len(dp)):
        dp[i] = min(dp[i-visitor] + cost, dp[i])
        if i >= c:
            min_invest = min(dp[i], min_invest)

print(min_invest)