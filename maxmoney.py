"""
Author : Revanth Sai Nandamuri
GitHUB : https://github.com/RevanthNandamuri1341b0
Date of update : 25 April 2021
Time of update : 17:17
Project name : MAX MONEY 
Domain : Competitive Programming in Python
Description : You are given a one dimensional array that may contain both positive and negative integers, find the sum of contiguous subarray of numbers which has the largest sum.
File ID : 048052
Modified by : #your name#
"""


def findMAXsubarray(A, N, B):
    sum = 0
    for i in range(N):
        A[i] = int(A[i])
        print(A[i])
        if(sum < B):
            sum += A[i]
        else:
            return sum-A[i-1]


T = int(input())
k = 0

while(k < T):
    A = []
    N, B = input().split(" ")
    N = int(N)
    B = int(B)
    A = input().split(" ")
    print(findMAXsubarray(A, N, B))
    k = k+1
