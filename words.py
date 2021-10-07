n = int(input())
#n = 3
#arr = ['arr_1', 'arr_2', 'arr_3']
arr = []
for i in range(0, n):
    x = input()
    arr.append(x)
bin = input()
res = [int(x) for x in str(bin)]


def swap(wrd):
    char_arr1 = []
    x = ""
    for i in wrd:
        if i == '_':
            char_arr1.append(x)
            char_arr1.append('_')
            x = ""
        else:
            x = x+i
    char_arr1.append(x)
    op = ""
    return op.join(char_arr1[::-1])


new_arr = []
cn = 0
for i in res:
    if i == 1:
        new_arr.append(swap(arr[cn]))
    else:
        new_arr.append(arr[cn])
    cn += 1
outP = ''.join(new_arr)

print(outP)
