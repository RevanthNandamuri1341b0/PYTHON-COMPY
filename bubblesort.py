"""
Author : Revanth Sai Nandamuri
GitHUB : https://github.com/RevanthNandamuri1341b0
Date of update : 25 April 2021
Time of update : 17:02
Project name : Bubble sort
Domain : Competitive Programming in Python
Description : Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
File ID : 907368
Modified by : #your name#
"""


def bs(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


array = [1, 25, 185, 65, 3, 3, 4, 78]

bs(array)
print(array)
