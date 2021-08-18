"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 15 August 2021
*Project name : Sum and Average 
*Domain : Python
*Description : Finding the sum and average of a list
*File Name : sum_avg.py
*File ID : 265395
*Modified by : #your name#
"""

def sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

def avg(arr,sum):
    return (sum/len(arr))

arr=[4, 5, 1, 2, 9, 7, 10, 8]
print("The SUM = ",sum(arr)," The Average = ",avg(arr,sum(arr)))
