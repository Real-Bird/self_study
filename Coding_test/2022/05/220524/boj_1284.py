while (s:=input()) != "0":
    width = 1
    for i in s:
        if i == "0":
            width += 5
        elif i == "1":
            width += 3
        else:
            width += 4
    print(width)