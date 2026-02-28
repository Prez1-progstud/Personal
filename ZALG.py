def priklad12(n):
    i = 1
    while i <= n:
        for j in range(1, i+1):
            print("*", end="")
        i *= 2
    print()

priklad12(15)

