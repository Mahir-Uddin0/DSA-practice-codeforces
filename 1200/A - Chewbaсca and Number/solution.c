#include<stdio.h>
long long power(int base, int exp){
    long long result=1;
    if(exp==0) return 1;
    for(int i=1; i<=exp; i++){
        result*=10;
    }
    return result;
}
int main(){
    long long x,y=0;
    scanf("%lld",&x);
    for(int i=0; x!=0; i++){
        if(x/10==0 && x==9) y = y + x*(long long)power(10,i);
        if(x%10>4) y+= (long long)power(10,i)*(9-x%10);
        else y+= x%10*(long long)power(10,i);
        x = x/10;
    }
    printf("%lld",y);
    return 0;
}
