                            #  NOT AN OPTIMIZED ONE

def findKth(a,n,k):
    d={}
    m=0
    for i in range(n):
        m=min(a)
        if k>1:
            d[m]=k
            a.remove(m)
        k-=1
    print(d)
    print(a)
    return m


if __name__ == "__main__":
    a=[12,3,5,7,19]
    # a=[7 ,10, 4 ,3, 20, 15]
    n=len(a)
    k=int(input("Which kth smallest element:"))
    ans=findKth(a,n,k)
    print("Kth smallest element is:",ans)