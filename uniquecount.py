"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 15 August 2021
*Project name : Count of unique values
*Domain : Python
*Description : Getting unique values and counting the recurrance 
*File Name : uniquecount.py
*File ID : 484919
*Modified by : #your name#
"""


def unique(arr):
    unique_arr = []
    for i in (arr):
        if i not in unique_arr:
            unique_arr.append(i)
    print("The unique elements are ", unique_arr)
    return unique_arr


def unique_count(arr, unique_arr):
    count_arr = []
    for i in unique_arr:
        count = 0
        for j in arr:
            if(i == j):
                count += 1
        str = i, ' = ', count
        count_arr.append(str)
    print(count_arr)


arr = [1, 2, 3, 54, 564, 6, 3432, 561, 5, 47654, 2314, 1,
       1, 1, 1, 1, 21, 3, 3, 3, 3, 4, 4, 55, 654, 3, 3, 33, 4]
print(arr)
unique_arr = unique(arr)
unique_count(arr, unique_arr)
