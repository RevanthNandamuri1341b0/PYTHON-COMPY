n1=int(input())
arr1 = map(int, input().strip().split())

n2=int(input())
arr2 = map(int, input().strip().split())

k=int(input())
c1=0
c2=0
for i in arr1:
    if i>k:
        c1+=1
        
for i in arr2:
    if i>k:
        c1+=1
print(max(c1,c2))
