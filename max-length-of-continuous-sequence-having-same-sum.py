                    #  BRUTE FORCE APPROACH
                    #  FOR LINEAR APPROACH REFER PART 2
def contSeq(a,b,n):
    res=0
    for i in range(n):
        s1=0
        s2=0
        for j in range(i,n):
            s1+=a[j]
            s2+=b[j]
            if s1==s2:
                res=max(res,j-i+1)
    return res



if __name__ == "__main__":
    x=[0, 1, 0, 1, 1, 1, 1]
    y=[1, 1, 1, 1, 1, 0, 1]
    # x=[0,0,0]
    # y=[1,1,1]
    # x=[0,0,1,0]
    # y=[1,1,1,1]
    ans=contSeq(x,y,len(x))
    print("Maximum length of contiguous sequence having same sum  is:",ans)