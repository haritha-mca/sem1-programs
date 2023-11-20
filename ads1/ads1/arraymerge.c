#include<stdio.h>
#include<stdlib.h>
void main()
{
int p,q,m,n,c;
int ar1[100],ar2[100],ar3[100];
printf("enter no of elements for array1:");
scanf("%d",&p);
printf("enter array elements:");
for(m=0;m<p;m++)
{
scanf("%d",&ar1[m]);
}

for(m=0;m<p;m++)
{
printf("%d",ar1[m]);
}

printf("enter no of elements for array2:");
scanf("%d",&q);
printf("enter array elements:");
for(n=0;n<q;n++)
{
scanf("%d",&ar2[n]);
}
m=0;
n=0;
c=0;
while((m<p)&&(n<q))
{
if(ar1[m]<ar2[n])
	ar3[c]=ar1[m++];
else
	ar3[c]=ar2[n++];
	c++;
}
while(m<p)
{
ar3[c]=ar1[m];
c++;
m++;
}
while(n<q)
{
ar3[c]=ar2[n];
c++;
n++;
}
printf("merged array:");
for(m=0;m<p+q;m++)
{
printf("%d",ar3[m]);
}
}


