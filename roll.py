num = int(input())
new_lst = []
for i in range(0, len(str(num)), 2):
    new_lst.append(str(num)[i: i + 2])
x = ""
if(len(str(num)) % 2 != 0):
    x = new_lst[-1]
    new_lst.remove(new_lst[-1])
op = []
for i in new_lst:
    if i[0] < i[1]:
        i = i.replace(i[0], "")
    else:
        i = i.replace(i[1], "")
    op.append(i)
op.append(x)

str = ""
for i in op:
    str += i
print(str)
