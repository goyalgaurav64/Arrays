import sys                      
def solve(a,k,n):
    sum=0
    res=sys.maxsize
    left=0
    for i in range(n):
        sum+=a[i]
        if i-left+1 >= k:
            res=min(res,sum)
            sum-=a[left]
            left+=1
    return res 



if __name__ == "__main__":
    # a=[2,3,1,2,4,3]
    # a=[10, 4, 2, 5, 6, 3, 8, 1]
    a=[1,4,2,10,23,3,1,0,20]
    k=int(input("Window size:"))
    ans=solve(a,k,len(a))
    print(ans)