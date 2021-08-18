"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 15 August 2021
*Project name : MINIMUM MAXIMUM and SECOND MINIMUM SECOND MAXIMUM 
*Domain : PYTHON
*Description : finding maximum, second_maximum, minimum, second_minimum
*File Name : min_max_1_2.py
*File ID : 707747
*Modified by : #your name#
"""


def sec_min(arr):
    arr.remove(min(arr))
    return min(arr)


def sec_max(arr):
    arr.remove(max(arr))
    return max(arr)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)
print("MAX = ", max(arr))
print("MIN = ", min(arr))
print("Second MAX = ", sec_max(arr))
print("Second MIN = ", sec_min(arr))
