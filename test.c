#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

void calculate_the_maximum(n,k){
 int maxand =0 , maxor= 0 , maxxor = 0;
    for(int i=1;i<n;i++)
    {
        for(int j=i+1;j<=n;j++)
        {
            int and = i & j ;
            int or = i | j ; 
            int xor = i ^ j ;

            if (and<k && and > maxand) { maxand= and;}
            if (or <k && or > maxor) { maxor = or;}
            if (xor < k && xor > maxxor) {maxxor = xor;}


        }
    }
    printf("%d\n",maxand);
    printf("%d\n",maxor);
    printf("%d\n",maxxor);

}

int main()
{
    int n, k;
    scanf("%d %d",&n, &k);
    calculate_the_maximum(n,k);

    return 0;
}