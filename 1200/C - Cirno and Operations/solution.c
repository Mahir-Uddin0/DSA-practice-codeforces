#include<stdio.h>

long long sum_func(long long* ptr, int size){
    long long sum=0;
    for(int i=0; i<size; i++){
        sum+=*(ptr+i);
    }
    return sum;
}
long long difference_sequence_sum(long long* arr, int size){
    long long total = (long long)(arr[size-1]-arr[0]);
    for(int i=0; i<size-1; i++){
        arr[i] = arr[i+1] - arr[i];
    }
    if(total<0) return total*(-1);
    else return total;
}

int main(){
    int t, size;
    long long total, sum=0;
    scanf("%d",&t);
    for(int i=1; i<=t; i++){
        scanf("%d",&size);
        long long arr[size];
        for(int j=0; j<size; j++){
            scanf("%lld",&arr[j]);
        }
        if(size==1){
            printf("%lld\n",arr[0]);
            continue;
        }
        sum=(long long)sum_func(arr,size);
        while(size>1){
            total = difference_sequence_sum(arr,size--);
            if(total>sum) sum = total;
        }
        printf("%lld\n",sum);
    }
    return 0;
}
