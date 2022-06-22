n, new, p = map(int, input().split())
if n == 0:
    print(1)
else:
    ranking = list(map(int, input().split()))
    if new <= ranking[-1] and n == p:
        print(-1)
    else:
        answer = n + 1
        for i in range(n):
            if ranking[i] <= new:
                answer = i + 1
                break

        print(answer)