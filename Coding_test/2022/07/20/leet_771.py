def numJewelsInStones(jewels: str, stones: str) -> int:
    table = {}
    cnt = 0
    for s in stones:
        if s not in table:
            table[s] = 1
        else:
            table[s] += 1

    for j in jewels:
        if j in table:
            cnt += table[j]
    return cnt


print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))