n = int(input())
if n == 1:
    print("Window")
if n < 38:
    n0 = (n - 2) % 4
    if n0 == 0 or n0 == 3:
        print("Window")
    else:
        print("Aisle")
