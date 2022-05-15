def solution(bricks, n, k):
    answer = 1e9
    for i in range(1, (x:=len(bricks[1:-1]))):
        temp = bricks.copy()
        tmp1 = temp[i]
        temp[i] = n
        if k > 2:
            for j in range(i+2, x):
                tmp2 = temp[j]
                temp[j] = n
                if x - temp.count(n) == k:
                    answer = min(answer, (n - tmp1) + (n - tmp2))
                temp[j] = tmp2
        else:
            if x - temp.count(n) == k:
                answer = min(answer, n - tmp1)
        temp[i] = tmp1
    return answer

print(solution([1, 2, 5, 3, 1, 0, 2, 3],6,3))
print(solution([0, 1, 2, 3, 4],5,2))
print(solution([0, 1, 2, 3, 4, 3],5,2))