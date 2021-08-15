"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 15 August 2021
*Project name : Swap two elements in a list
*Domain : PYTHON
*Description : Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
*File Name : element_swap.py
*File ID : 505654
*Modified by : #your name#
"""


def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]


arr = [1, 2, 3, 4, 5, 6]
pos1 = 1
pos2 = 4
print(arr)
swap(arr, pos1-1, pos2-1)
print(arr)
