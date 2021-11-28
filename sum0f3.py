"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 28 November 2021
*Project name : Sum of 3
*Domain : Python
*Description : given an array of N integers and int k find out if there are 3 numbers that together sum up to k
*File Name : sum0f3.py
*File ID : 875536
*Modified by : #your name#
"""

arr = list(map(int, input().split()))
x = int(input("Enter The number : "))
for i in arr:
    for j in arr:
        if(arr.index(j) <= arr.index(i)):
            continue
        for k in arr:
            if((arr.index(k) <= arr.index(i)) or (arr.index(k) <= arr.index(j))):
                continue
            if(i+j+k == x):
                print(i, j, k)
