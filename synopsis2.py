x1, y1 = input("X1 ,Y1 = ")
x2, y2 = input("X2 ,Y2 = ")
print("Quardinates of first rectangle: ")
print(f"({x1},{y1}),({x2},{y2}),({x1},{y2}),({x1},{y2})")

x3, y3 = input("X3 ,Y3 = ")
x4, y4 = input("X4 ,Y4 = ")
print("Quardinates of second rectangle: ")
print(f"({x3},{y3}),({x4},{y4}),({x3},{y4}),({x4},{y3})")

if(x1<x3<x2):
    if(y1<y3<y2):
        