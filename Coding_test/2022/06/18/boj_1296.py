yeondo = input().rstrip()
n = int(input())
team_name = [input() for _ in range(n)]
team_name.sort()
max_rate = max_idx = 0

for i in range(n):
    L = yeondo.count("L") + team_name[i].count("L")
    O = yeondo.count("O") + team_name[i].count("O")
    V = yeondo.count("V") + team_name[i].count("V")
    E = yeondo.count("E") + team_name[i].count("E")
    rate = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if max_rate < rate:
        max_rate = rate
        max_idx = i
print(team_name[max_idx])