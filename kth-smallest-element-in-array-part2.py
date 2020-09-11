def kthSmallest(a,n,k):
    a.sort()
    return a[k-1]



if __name__ == "__main__":
    a=[12,3,5,7,19]
    k=int(input("Kth smallest element:"))
    ans=kthSmallest(a,len(a),k)
    print("Kth smallest element is:",ans)