n = int(input())
dice = list(map(int, input().split()))

if n == 1:
    dice.sort()
    print(sum(dice[:5]))
    exit(0)
min_dice = [min(dice[i], dice[-(i+1)]) for i in range(3)]
min_dice.sort()

a = (min_dice[0] * n ** 2) * 2
b = ((min_dice[1] * n * 2) + (min_dice[0] * n * (n - 2))) * 2
c = (min_dice[2] * 4) + (min_dice[1] * (n-2) * 4) + (min_dice[0] * (n - 2) * (n - 2))

print(a + b + c)