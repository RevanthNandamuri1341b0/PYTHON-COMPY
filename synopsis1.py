n = float(input())
g = float(input())

if n % g == 0:
    print(n)
else:
    n1 = round(n % g)
    n = n-n1
    print(n1)
    if n % g == 0:
        print("done", n)
    else:
        print("Not done")
