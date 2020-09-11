def count1s(a,n,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if(a[mid]==1 and (mid==high or a[mid+1]==0)):
            return mid+1
        if a[mid]==1:
            return count1s(a,n,mid+1,high)
        return count1s(a,n,low,mid-1)
    return 0


if __name__ == "__main__":
    # a=[1, 1, 1, 1, 0, 0, 0]
    # a=[0, 0, 0, 0, 0, 0, 0]
    a=[1, 1, 1, 1, 1, 1, 1]
    ans=count1s(a,len(a),0,len(a)-1)
    print("Number of 1s in the sorted binary array are:",ans)