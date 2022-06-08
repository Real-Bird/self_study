n = int(input())
file_size = list(map(int, input().split()))
cluster = int(input())
answer = 0

for i in file_size:
    if i % cluster == 0:
        answer += i//cluster
    else:
        answer += i//cluster+1

print(answer * cluster)