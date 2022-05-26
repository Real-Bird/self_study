while True:
    tree = list(map(int, input().split()))
    if tree[0] == 0:
        break
    leaf = 1
    for i in range(1, len(tree), 2):
        leaf = leaf * tree[i] - tree[i+1]
    print(leaf)