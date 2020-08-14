#include<stdio.h>
void swap(int *a,int *b)
{
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
}
int main()
{
    int a[10],n,i,flag=0;  //for flag =0 i m expecting the '<' relation
    printf("Enter size of array:");
    scanf("%d",&n);
    printf("Enter Array Elements:\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Original Array is:\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    for(i=0;i<n;i++)
    {
        if(flag)
        {
            if(a[i]<a[i+1])
            {
                swap(&a[i],&a[i+1]);
            }
        }
        else
        {
            if(a[i]>a[i+1])
            {
                swap(&a[i],&a[i+1]);
            }
        }
        flag=!flag;
    }
    printf("\nZig Zag array is:\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}