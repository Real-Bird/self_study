n, m = map(int, input().split())
boxs = sum(list(map(int, input().split())))
books = sum(list(map(int, input().split())))
print(boxs - books)