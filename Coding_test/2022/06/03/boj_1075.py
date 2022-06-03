def changeNum(n):
    n = list(n)
    length = len(n)
    return int("".join(n[:length-2]) + "0"*2)

n = input()
f = int(input())
tmp = changeNum(n)

while True:
    if tmp % f == 0:
        break
    tmp += 1

tmp = str(tmp)
print(tmp[len(tmp)-2:].zfill(2))

# 코드 수정
# n = input()
# f = int(input())
# tmp = int(n[:-2] + "00")
#
# while True:
#     if tmp % f == 0:
#         break
#     tmp += 1
#
# tmp = str(tmp)
# print(tmp[-2:].zfill(2))