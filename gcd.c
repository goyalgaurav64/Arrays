#include<stdio.h>
int main()
{
    int x,y,i;
    printf("Enter first number:");
    scanf("%d",&x);
    printf("Enter second number:");
    scanf("%d",&y);
    int min;
    if(x<y)
    min=x;
    else
    min=y;
    
    for(i=min;i>=1;i--)
    {
        if(x%i==0 && y%i==0)
        {
            break;
        }
    }
    printf("HCF of %d and %d is:%d",x,y,i);
}