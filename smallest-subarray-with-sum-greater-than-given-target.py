import sys
def subarray(a,k,n):
    res=sys.maxsize
    left,s=0,0
    for i in range(n):
        s+=a[i]
        while s > k:
            res=min(res,i-left+1)
            s-=a[left]
            left+=1
    return res if res is not sys.maxsize else -1

if __name__ == "__main__":
    a=[1, 4, 45, 6, 0, 19]
    k=int(input("Given Target:"))
    ans=subarray(a,k,len(a))
    print("Smallest subarray whose sum is greater than the given target having length is:",ans)