from collections import Counter

guest = int(input())
seat = list(map(int, input().split()))
c = Counter(seat).most_common()
cnt = 0
for i in c:
    if i[1] > 1:
        cnt += i[1] - 1

print(cnt)