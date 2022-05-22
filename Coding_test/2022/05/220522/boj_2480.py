from collections import Counter
dice = list(map(int, input().split()))
dice.sort(reverse=True)
cnt = Counter(dice).most_common()
if cnt[0][1] == 3:
    print(10_000+(cnt[0][0]*1000))
elif cnt[0][1] == 2:
    print(1_000+(cnt[0][0]*100))
else:
    print(cnt[0][0]*100)