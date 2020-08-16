def printSpiral(m):
    rows=len(m)
    cols=len(m[0])
    lr=rows-1
    lc=cols-1
    r=0
    c=0
    while(r<=lr and c<=lc):
        for i in range(c,lc+1):
            print(m[r][i],end=' ')
        r+=1
        print()
        for i in range(r,lr+1):
            print(m[i][lc],end=' ')
        lc-=1
        print()
        if r<=lr:
            for i in range(lc,c-1,-1):
                print(m[lr][i],end=' ')
            lr-=1
        if c<=lc:
            for i in range(lr,r-1,-1):
                print(m[i][c],end=' ')
            c+=1






if __name__ == "__main__":
    m=[['a','b','c','d','e'],
    ['f','g','h','i','j'],
    ['u','v','m','n','o'],
    ['p','q','r','s','t']]
    printSpiral(m)