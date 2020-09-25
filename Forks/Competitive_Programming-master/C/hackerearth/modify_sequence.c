/* Suppose we have a sequence of non-negative integers, Namely a_1, a_2, ... ,a_n. 
At each time we can choose one term a_i with 0 < i < n and we subtract 1 from both a_i and a_i+1. 
Find whether we can get a sequence of all zeros after several operations.

Input: The first line of test case is a number N. (0 < N <= 10000) The next line is N non-negative integers, 0 <= a_i <= 109
Output:If it can be modified into all zeros with several operations output “YES” in a single line, otherwise output “NO” instead.


SAMPLE INPUT:
2
1 2

SAMPLE OUTPUT:
NO */
#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int a[n],i,flag=0,temp;
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    if(n==1)
        flag=(a[0]==0?1:0);
    else if(n==2)
        flag=(a[0]==a[1]?1:0);
    else if(n%2!=0)
        flag=0;
    else{ 
        for(i = n - 2 ; i >= 0 ; i--){		
		    if(a[i] != 0){
			    if(a[i] >= a[i + 1]){
				    a[i] -= a[i + 1] ;
				    a[i + 1] = 0 ;
				    flag=1;
			    }
			    else{
				    flag=0;
				    break;
			    }
		    }
	    }
    }
    if(flag==1)
        printf("YES");
    else
        printf("NO");
    return 0;
}
