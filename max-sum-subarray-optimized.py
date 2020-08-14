def subArr(ar,n,k):
    msum=0
    wsum=0
    for i in range(0,k):
        wsum+=ar[i]
    for j in range(k,n):
        wsum+=ar[j]-ar[j-k]
        msum=max(msum,wsum)
    return msum


if __name__ == "__main__":
    ar=list(map(int,input("Enter Array Values:").split(" ")))
    k=int(input('Enter Length of Sub Array:'))
    n=len(ar)
    ans=subArr(ar,n,k)
    print('Max sum is:',ans)