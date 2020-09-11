def firstAndlastOccur(a,n,k):
    first,last=-1,-1
    for i in range(n):
        if a[i]!=k:
            continue
        else:
            if first==-1:
                first=i
        last=i
    if first != -1:
        print("First occurence is:",first)
        print("Last occurence is:",last)
    else:
        print("Element not found")



if __name__ == "__main__":
    a=[1, 3, 5, 5, 5, 5, 67, 123, 125]
    k=int(input("Which element:"))
    firstAndlastOccur(a,len(a),k)