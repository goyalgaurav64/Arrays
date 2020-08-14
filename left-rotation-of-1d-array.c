#include<stdio.h>
int main()
{
    void leftRot(int a[],int n);
    int a[10];
    int i,n;
    printf("Enter size of array:");
    scanf("%d",&n);
    printf("\nEnter Elements:\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("\nArray is:\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    leftRot(a,n);
}
void leftRot(int a[],int n)
{
    void disp(int a[],int n);
    int temp,shift;
    printf("\nHow Many Rotations:\n");
    scanf("%d",&shift);
    while(shift)
    {
        temp=a[0];
        for(int i=0;i<=n-2;i++)
        {
            a[i]=a[i+1];
        }
        a[n-1]=temp;
        shift--;
    }
    disp(a,n);
}
void disp(int a[],int n)
{
    for(int i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}