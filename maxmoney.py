def findMAXsubarray(A,N,B):
    sum=0
    for i in range(N):
        A[i]=int(A[i])
        print(A[i])
        if(sum<B):
            sum+=A[i]
        else:
            return sum-A[i-1]
T=int(input())
k=0

while(k<T):
    A=[]
    N,B = input().split(" ")
    N=int(N)
    B=int(B)
    A=input().split(" ")
    print(findMAXsubarray(A,N,B))
    k=k+1
