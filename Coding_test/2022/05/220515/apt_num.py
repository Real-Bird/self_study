from collections import deque


def bfs(graph, a, b):
    n = len(graph)
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt


n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph, i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
