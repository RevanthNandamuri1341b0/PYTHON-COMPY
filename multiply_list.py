"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 15 August 2021
*Project name : Element multiplication 
*Domain : PYTHON
*Description : Multiplying each element 
*File Name : multiply_list.py
*File ID : 498014
*Modified by : #your name#
"""


def multiply(arr):
    mul = 1
    for i in arr:
        mul *= i
    return mul


arr = [1, 2, 3, 4, 5, 6]
print(arr, " = ", multiply(arr))
