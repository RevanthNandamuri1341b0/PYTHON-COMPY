"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 25 October 2021
*Project name : alphabet pattern
*Domain : Python
*Description :      
todo                    A
todo                    B B
todo                    C C C
*File Name : alphabetpattern1.py
*File ID : 213546
*Modified by : #your name#
"""

n = int(input())


def alpha1(n):
    num = 65
    for i in range(0, n):
        for i in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
        num += 1
        print()


alpha1(n)
