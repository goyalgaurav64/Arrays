def moveZeroes(a,n):
    cnt=0
    for i in range(n):
        if a[i]!=0:
            a[cnt]=a[i]
            cnt+=1
    for i in range(cnt,n):
        a[i]=0
    print(a)



if __name__ == "__main__":
    # a=[1, 2, 0, 4, 3, 0, 5, 0]
    # a=[1, 2, 0, 0, 0, 3, 6]
    a=[1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    moveZeroes(a,len(a))