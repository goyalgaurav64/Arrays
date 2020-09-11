def first(a,x,low,high,n):
    if low <= high:
        mid=low+(high-low)//2
        if (mid==0 or a[mid-1] < x) and a[mid]==x:
            return mid
        elif x > a[mid]:
            return first(a,x,mid+1,high,n)
        return first(a,x,low,mid-1,n)
    return -1

def last(a,x,low,high,n):
    if low <= high:
        mid=low+(high-low)//2
        if (mid==n-1 or x<a[mid+1]) and a[mid]==x:
            return mid
        elif x < a[mid]:
            return last(a,x,low,mid-1,n)
        return last(a,x,mid+1,high,n)
    return -1




if __name__ == "__main__":
    a=[1,3,5,5,5,5,67,123,125]
    k=int(input("Which element:"))
    print("First occurence is:",first(a,k,0,len(a)-1,len(a)))
    print("Last occurence is:",last(a,k,0,len(a)-1,len(a)))