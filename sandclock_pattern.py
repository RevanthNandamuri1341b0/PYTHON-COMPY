"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 25 August 2021
*Project name : Sand Clock Pattern
*Domain : PYTHON
*Description : 
                * * * * *
                  * * *
                    *
                  * * *
                * * * * *
*File Name : sandclock_pattern.py
*File ID : 991237
*Modified by : #your name#
"""
def sandclock(n):
    for i in range(n,0,-1):
        if(i%2!=0):
            for j in range(0,n-i):
                print("",end=" ")
            for k in range(0,i):
                print(" *",end="")
            print()
    
    for a in range(0,n+1):
        if(a%2!=0):
            for b in range(0,n-a):
                print("",end=" ")
            for c in range(0,a):
                print(" *",end="")
            print()
            


n=int(input())
#n=5
sandclock(n)