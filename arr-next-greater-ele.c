#include<stdio.h>
void NextGreater(int a[],int n);
void NextGreater(int a[],int n)
{
    int i,j;
    int next=0;
    for(i=0;i<n;i++)
    {
        next=-1;
        for(j=i+1;j<n;j++)
        {
            if(a[j]>a[i])
            {
                next=a[j];
                break;
            }
        }
        printf("%d->%d\n",a[i],next);
    }
}



int main()
{
    int ar[]={12,1,0,17,10};
    int n=sizeof(ar)/sizeof(ar[0]);
    NextGreater(ar,n);
}