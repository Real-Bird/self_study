from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))
queue = deque([i for i in range(1, n + 1)])
cnt = 0

for num in nums:
    while True:
        if queue[0] == num:
            queue.popleft()
            break
        else:
            if queue.index(num) < len(queue) / 2:
                while queue[0] != num:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != num:
                    queue.appendleft(queue.pop())
                    cnt += 1

print(cnt)
