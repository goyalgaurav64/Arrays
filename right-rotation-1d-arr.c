#include<stdio.h>
void show(int a[],int n);
void rightRot(int a[],int n);
void disp(int a[],int n);
int main()
{
    int n,a[10],i;
    printf("Enter size of array:");
    scanf("%d",&n);
    printf("Enter Array elements:\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    show(a,n);
}
void show(int a[],int n)
{
    int i;
    printf("\nArray is:\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    rightRot(a,n);
}
void rightRot(int a[],int n)
{
    int temp,shift,i;
    printf("\nHow Many Shifts:");
    scanf("%d",&shift);
    while(shift)
    {
        temp=a[n-1];
        for(i=n-1;i>=1;i--)
        {
            a[i]=a[i-1];
        }
        a[0]=temp;
        shift--;
    }
    disp(a,n);
}
void disp(int a[],int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}