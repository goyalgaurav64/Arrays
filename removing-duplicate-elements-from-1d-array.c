#include<stdio.h>
int main()
{
    int n,a[10],i,j=0,temp[10],count=0;
    printf("Enter size of array:");
    scanf("%d",&n);
    printf("Enter Elements in sorted order:\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Original Array is:\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    for(i=0;i<n-1;i++)
    {
        if(a[i]!=a[i+1])
        {
            a[j]=a[i];
            j++;
            count++;
        }
    }
    a[j]=a[n-1];
    printf("\nAfter removing Dupliacte Elements:\n");
    for(j=0;j<=count;j++)
    {
        printf("%d ",a[j]);
    }
}