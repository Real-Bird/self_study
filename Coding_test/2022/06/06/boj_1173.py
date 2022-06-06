N, m, M, T, R = map(int, input().split())
total_time, workout_time = 0, 0
now = m

if now > M or now + T > M:
    print(-1)
    exit()

while workout_time < N:
    if now + T <= M:
        now += T
        total_time += 1
        workout_time += 1
    else:
        while now + T > M:
            now -= R
            if now < m:
                now = m
            total_time += 1

print(total_time)