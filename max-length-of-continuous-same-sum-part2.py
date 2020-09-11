def contSeq(a,b,n):
    d={}
    s1,s2,res=0,0,0
    for i in range(n):
        s1+=a[i]
        s2+=b[i]
        dif=s1-s2
        if dif not in d:
            d[dif]=i
        else:
            res=max(res,i-d[dif])
    print(d)
    return res


if __name__ == "__main__":
    # x=[0, 1, 0, 1, 1, 1, 1]
    # y=[1, 1, 1, 1, 1, 0, 1]
    # x=[0,0,0]
    # y=[1,1,1]
    x=[0,0,1,0]
    y=[1,1,1,1]
    ans=contSeq(x,y,len(x))
    print("Maximum length of contiguous sequence having same sum  is:",ans)