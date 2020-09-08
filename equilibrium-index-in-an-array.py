def equilibrium(a,n):
    i=0
    j=n
    flag=False
    sm,ls=0,0
    sm=sum(a)
    while i<j:
        sm-=a[i]
        if sm==ls:
            flag=True
            break                               #  O(n)
        ls+=a[i]
        i+=1
    if flag:
        return i
    return -1



if __name__ == "__main__":
    a=[1,7,3,6,5,6]
    # a=[1,2,3]
    # a=[-7, 1, 5, 2, -4, 3, 0]
    ans=equilibrium(a,len(a))
    if ans>=0:
        print("Equilibrium exists at:",ans)
    else:
        print("-1")