"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 25 August 2021
*Project name : Finding missing number
*Domain : PYTHON
*Description : You are given an array of positive numbers 
               from 1 to n, such that all numbers from 
               1 to n are present except one number x. 
               You have to find x.The input array is not sorted.
               Runtime Complexity: O(n)
*File Name : amazon_interview_question1.py
*File ID : 799173
*Modified by : #your name#
"""

def amazon_unique(n,arr):
    a_list = list(range(1, n+1))
    print(a_list)
    for i in a_list:
        if i not in arr:
            print(i)       


n=int(input())
arr= list(map(int,input().strip().split()))
#print(arr)
amazon_unique(n,arr)
