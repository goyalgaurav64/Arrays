#include<stdio.h>
#include<stdlib.h>
int findCand(int a[],int n);
int noOfOccurences(int cand,int a[],int n);
int main()
{
    int a[]={1,3,1,3,2,3,3,2};
    int n=sizeof(a)/sizeof(a[0]);
    int cand=findCand(a,n);
    int num=noOfOccurences(cand,a,n);
    if(num > n/2)
    {
        printf("%d occuring %d times",cand,num);
    }
    else
    {
        printf("No Majority element");
    }
    
}
int findCand(int a[],int n)
{
    int idx=0;
    int count=1;
    for(int i=1;i<n;i++)
    {
        if(a[idx]==a[i])
        {
            count++;
        }
        else
        {
            count--;
        }
        if(count==0)
        {
            idx=i;
            count=1;
        }
    }
    return a[idx];
}
int noOfOccurences(int cand,int a[],int n)
{
    int c=0;
    for(int i=0;i<n;i++)
    {
        if(cand==a[i])
        {
            c++;
        }
    }
    return c;
}