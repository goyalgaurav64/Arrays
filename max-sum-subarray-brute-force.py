def subArr(ar,n,k):          
    maxi=0               #denotes maximum sum of sub array
    for i in range(0,n-k+1):
        wsum=0                  #denotes Sub Array Sum
        for j in range(i,i+k):
            wsum+=ar[j]
            maxi=max(wsum,maxi)
    return maxi


if __name__ == "__main__":
    ar=list(map(int,input("Enter Array Values:").split(" ")))
    k=int(input('Enter Length of Sub Array:'))
    n=len(ar)
    ans=subArr(ar,n,k)
    print('Max sum is:',ans)