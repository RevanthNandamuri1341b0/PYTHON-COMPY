"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 15 August 2021
*Project name : Check if element exists
*Domain : PYTHON
*Description : To search an element in list using Python
*File Name : Elementswap.py
*File ID : 272134
*Modified by : #your name#
"""


def exist(arr, element):
    if element in arr:
        print("EXISTS")
    else:
        print("NON")


arr = [1, 2, 4, 6, 7, 8, 96, 4534, 2, 24, 5]

x = 2
exist(arr, x)

x = 11
exist(arr, x)
