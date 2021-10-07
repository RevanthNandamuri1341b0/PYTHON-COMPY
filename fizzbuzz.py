"""
Author : Revanth Sai Nandamuri
GitHUB : https://github.com/RevanthNandamuri1341b0
Date of update : 25 April 2021
Time of update : 17:13
Project name : FizzBuzz
Domain : Competitive Programming in Python
Description : Write a program that prints n numbers . But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
File ID : 781927
Modified by : #your name#
"""


def fB(n):
    op = []
    for i in range(1, n+1):
        if ((i % 3 == 0) and (i % 5 == 0)):
            op.append("FizzBuzz")
        elif (i % 3 == 0):
            op.append("Fizz")
        elif (i % 5 == 0):
            op.append("Buzz")
        else:
            op.append(str(i))
    for i in op:
        print(i)


num = int(input("Enter a number : "))
fB(num)
