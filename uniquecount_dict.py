"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 15 August 2021
*Project name : Count of unique values
*Domain : Python
*Description : Getting unique values and counting the recurrance adding in dictionary 
*File Name : uniquecount_dict.py
*File ID : 484919
*Modified by : #your name#
"""


def unique(arr):
    unique_arr = []
    for i in (arr):
        if i not in unique_arr:
            unique_arr.append(i)
    return unique_arr


def unique_count(arr, unique_arr):
    dict = {}
    for i in unique_arr:
        count = 0
        for j in arr:
            if(i == j):
                count += 1
        dict[i] = count
    # print(dict)
    return dict


arr = [1, 2, 3, 4, 5, 6, 6, 6, 65, 6, 6, 5, 1,
       1, 1, 1, 1, 3, 3, 3, 3, 4, 4, 3, 3, 33, 4]
print("The array is ", arr)
print("The unique elements are ",  unique(arr))
print("The Count of the elements are ", unique_count(arr,  unique(arr)))

