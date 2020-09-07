# a=[1,1,-3,4,2]
# a=[2,1,-3,4,2]
a=[3,4,-1,4,3,-6,-7,2]
n=len(a)
c=0
found=False
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=a[j]
        if(sum==0):
            found=True
            c+=1
            break
if found:
    print("Found",c)
else:
    print("Not found")