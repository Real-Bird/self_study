def maxProfit(prices):
    min_price = int(1e9)
    max_profit = 0
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit

print(maxProfit([3,3,5,0,0,3,1,4]))