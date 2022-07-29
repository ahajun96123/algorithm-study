#include <stdio.h>


int main(){

    long long int N;
    scanf("%d",&N);

    long long int num = 1;

    for(long long int i=1; i<=N; i++){
        num=num*i;
        while(num % 10 == 0) num /= 10;

        num %= 1000000000000;
    }

    num %= 100000;
  
    if(num/10000==0) printf("%d",0);
    if(num/1000==0) printf("%d",0);
    if(num/100==0) printf("%d",0);
    if(num/10==0) printf("%d",0);
    printf("%d\n",num);

    return 0;
}