"""
Author : Revanth Sai Nandamuri
GitHUB : https://github.com/RevanthNandamuri1341b0
Date of update : 25 April 2021
Time of update : 17:11
Project name : Factorial 
Domain : Competitive Programming in Python
Description : A factorial is a function that multiplies a number by every number below it.
File ID : 475114
Modified by : #your name#
"""


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


num = int(input("Enter the number : "))
print(factorial(num))
