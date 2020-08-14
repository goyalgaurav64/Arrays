def maxSubArray(a,n):
    msum=a[0]
    tsum=a[0]
    for i in range(1,n):
        tsum=max(a[i],a[i]+tsum)
        msum=max(tsum,msum)
    return msum




if __name__ == "__main__":
    a=[2,-3,4,2]
    n=len(a)
    sum=maxSubArray(a,n)
    print("Maximum sum is:",sum)