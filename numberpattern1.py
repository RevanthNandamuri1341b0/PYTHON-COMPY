"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 06 November 2021
*Project name : unique number pattern
*Domain : PYTHON
*Description : 
1
121
1331
*File Name : numberpattern1.py
*File ID : 402135
*Modified by : #your name#
"""


from math import factorial


def tri(n):
    for i in range(n):
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()
        # for j in range(n-i+1):
        #     print(end=" ")


x = int(input())
a = []
for i in range(0, x):
    a[i] = int(input())

for i in a:
    tri(i)
