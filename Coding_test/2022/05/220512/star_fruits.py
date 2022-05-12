# 스타후르츠
def star_fruits():
    n, t, c, p = map(int, input().split())
    cnt = 0
    for i in range(t+1, n+1, t):
        cnt += 1
    print(cnt * c * p)
star_fruits()