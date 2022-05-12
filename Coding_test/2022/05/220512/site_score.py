#Site Score
def site_score():
    ur, tr, uo, to = map(int, input().split())
    print((56*ur)+(24*tr)+(14*uo)+(6*to))
site_score()