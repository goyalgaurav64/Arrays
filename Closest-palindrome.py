def closetPalin(num):
    #  CASE 1  :  lpnum is the largest palindrome which will be less than the given number
    lpnum=num-1
    while(not isPalin(convertNumtoStr(abs(lpnum)))):
        lpnum-=1
    
    #  CASE 2  :  spnum is the smallest palindrome which will be greater than the given number
    spnum=num+1
    while(not isPalin(convertNumtoStr(abs(spnum)))):
        spnum+=1

    if(abs(num-lpnum) <= abs(num-spnum)):
        return lpnum
    return spnum

def isPalin(s):
    for i in range(len(s)//2):
        if(s[i]!=s[-1-i]):
            return False
    return True
    
def convertNumtoStr(num):
    s=str(num)
    return s


if __name__ == "__main__":
    n=int(input("Give any number:"))  #  114
    ans=closetPalin(n)
    print("Closet Palindrome to %d is %d"%(n,ans))