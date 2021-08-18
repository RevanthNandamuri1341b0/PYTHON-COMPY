"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 15 August 2021
*Project name : EVEN AND ODD
*Domain : PYTHON
*Description : Print all even and odd elements in a list And count them
*File Name : even_odd.py
*File ID : 141554
*Modified by : #your name#
"""


def even_odd(arr):
    odd = []
    eve = []
    for i in arr:
        if(i % 2 == 0):
            eve.append(i)
        else:
            odd.append(i)
    print(odd)
    print("Length = ",len(odd))
    
    print(eve)
    print("Length = ",len(eve))


arr = [1, 2, 3, 4, 5, 7, 6, 4, 3, 6, 78, 53, 3, 5, 6]
even_odd(arr)
