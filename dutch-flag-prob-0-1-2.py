def dutchFlag(ar,n):
    low=0
    high=n-1
    mid=0       #it'll traverse the whole array
    while mid<=high:
        if ar[mid]==0:
            ar[low],ar[mid]=ar[mid],ar[low]
            low+=1
            mid+=1
        elif ar[mid]==1:
            mid+=1
        else:
            ar[high],ar[mid]=ar[mid],ar[high]
            high-=1
    return ar




if __name__ == "__main__":
    ar=list(map(int,input("Enter array containing (0,1,2):").split(',')))
    n=len(ar)
    res=dutchFlag(ar,n)
    print("Segregated Array:",res)


