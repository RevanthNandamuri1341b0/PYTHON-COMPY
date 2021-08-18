"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 15 August 2021
*Project name : Sum of number digits in List
*Domain : PYTHON
*Description : sum of digits inside each element of a list
*File Name : digit_sum.py
*File ID : 054066
*Modified by : #your name#
"""

def digitsum(arr):
    dig=[]
    for i in arr:
        sum=0
        for j in str(i):
            sum += int(j)
        dig.append(sum)
    return dig

arr=[41,52,73,45,53,62]
print("Q = ",arr)
print("A = ",digitsum(arr))