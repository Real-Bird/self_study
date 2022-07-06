def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
nodes = list(map(int, input().split()))
del_node = int(input())
cnt = 0

dfs(del_node, nodes)

for i in range(n):
    if nodes[i] != -2 and i not in nodes:
        cnt += 1

print(cnt)