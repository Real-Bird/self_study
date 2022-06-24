import datetime
current_year, current_month, corrent_day = map(int, input().split())
d_year, d_month, d_day = map(int, input().split())
now = datetime.date(current_year,current_month,corrent_day)
D_Day = datetime.date(d_year,d_month,d_day)
rest = (D_Day - now).days

if rest > 365242:
    print("gg")
else:
    print(f"D-{rest}")