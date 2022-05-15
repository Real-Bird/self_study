from collections import deque

def solution(n, text, second):
    led = ["_"] * n
    for i in text:
        led.append(i)
    q = deque(led)
    answer = ''
    cnt = 0
    while True:
        if cnt == second:
            break
        temp = q.popleft()
        q.append(temp)
        cnt += 1
    a = list(q)
    return answer.join(a[:n]).replace(" ", "_")

print(solution(6, "hi bye", 1))
print(solution(6, "hi bye", 2))
print(solution(6, "hi bye", 6))