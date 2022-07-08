n = int(input()) # 크레인
crane_weights = list(map(int, input().split())) # 크레인 무게 제한
m = int(input()) # 박스
box_weights = list(map(int, input().split())) # 박스 무게 제한

crane_weights.sort(reverse=True)
box_weights.sort(reverse=True)

checked = [False for _ in range(m)]
time = 0
cnt = 0
position = [0] * n
if box_weights[0] > crane_weights[0]:
    time = -1
else:
    while cnt < m:
        for i in range(n):
            while position[i] < m:
                if not checked[position[i]] and crane_weights[i] >= box_weights[position[i]]:
                    checked[position[i]] = True
                    position[i] += 1
                    cnt += 1
                    break
                position[i] += 1
        time += 1

print(time)