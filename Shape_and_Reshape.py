import numpy

arr = input().strip().split(' ')
arr_new = numpy.array(arr, int)
print(numpy.reshape(arr_new, (3, 3)))
