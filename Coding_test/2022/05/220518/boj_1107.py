n = int(input())
m = int(input())
broken_btn = list(map(int,input().split()))
min_cnt = abs(100-n)

for i in range(1_000_001):
    nums = str(i)
    for j in range(x:=len(nums)):
        if int(nums[j]) in broken_btn:
            break
        elif j == x - 1:
            min_cnt = min(min_cnt, abs(i-n+x))

print(min_cnt)