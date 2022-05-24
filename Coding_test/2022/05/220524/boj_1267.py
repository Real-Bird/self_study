n = int(input())
call = list(map(int, input().split()))
min_fee_y = 0
min_fee_m = 0
for i in range(len(call)):
    min_fee_y += call[i] // 30 * 10 + 10
    min_fee_m += call[i] // 60 * 15 + 15

if min_fee_y < min_fee_m:
    print(f"Y {min_fee_y}")
elif min_fee_y > min_fee_m:
    print(f"M {min_fee_m}")
else:
    print(f"Y M {min_fee_m}")