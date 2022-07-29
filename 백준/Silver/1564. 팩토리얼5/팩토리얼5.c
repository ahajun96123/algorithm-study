#include <stdio.h>


int main(){

    long long int N;
    scanf("%d",&N);

    long long int num=1;

        for(long long int i=1; i<=N; i++){
        num=num*i;
        while(num%10==0) num=num/10;

        //if((i+1)/1000000==0) num=num%100000000000;
        //else if((i+1)/100000==0) num=num%10000000000;
        //else if((i+1)/10000==0) num=num%1000000000;
        //else if((i+1)/1000==0) num=num%100000000;
        //else if((i+1)/100==0) num=num%10000000;
        //else if((i+1)/10==0) num=num%1000000;
        //else num=num%1000000000;
        num=num%1000000000000;
    }

    num=num%100000;

    if(num/10000==0) printf("%d",0);
    if(num/1000==0) printf("%d",0);
    if(num/100==0) printf("%d",0);
    if(num/10==0) printf("%d",0);
    printf("%d\n",num);

    return 0;
}