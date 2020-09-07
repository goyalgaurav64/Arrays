def FindSubarray(a,n,k):
    d={0:1}
    s=0
    cnt=0
    for i in a:
        s+=i

        if s-k in d:
            cnt+=d[s-k]
        if s in d:
            d[s]+=1
        else:
            d[s]=1
    return cnt




if __name__ == "__main__":
    a=[3,4,7,2,-3,1,4,2]
    k=int(input("Enter required sum:"))
    cnt=FindSubarray(a,len(a),k)
    print("Subarray with given sum:",cnt)