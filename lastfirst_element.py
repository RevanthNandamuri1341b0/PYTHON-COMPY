"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 15 August 2021
*Time of update : 14:31
*Project name : FIRST LAST SWAP
*Domain : PYTHON
*Description : Python program to interchange first and last elements in a list
*File Name : lastfirst_element.py
*File ID : 592892
*Modified by : #your name#
"""


def firstlast_1(arr):
    n = len(arr)
    temp = arr[0]
    arr[0] = arr[n-1]
    arr[n-1] = temp


def firstlast_2(arr):
    arr[0], arr[-1] = arr[-1], arr[0]


arr = [1, 2, 3, 4, 5, 6]
print(arr)
# firstlast_1(arr)
firstlast_2(arr)
print(arr)
