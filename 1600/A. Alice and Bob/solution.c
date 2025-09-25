#include<stdio.h>
#include<stdbool.h>

int gcd_two(int a, int b){
    while(true){
        int temp = b;
        b = a%b;
        a = temp;
        if(b == 0) break;
    }
    return a;
}

int gcd_multi(int* arr, int n){
    int gcd_intermediate = arr[0];
    for(int i=0; i<n-1; i++){
        gcd_intermediate = gcd_two(arr[i+1], gcd_intermediate);
        if(gcd_intermediate == 1) break;
    }
    return gcd_intermediate;
}

int main(){
    int n,temp;
    scanf("%d",&n);
    int arr[n];
    
    for(int i=0; i<n; i++){
        scanf("%d",&arr[i]);
    }
    
    int max = arr[0];
    for(int i=1; i<n; i++) if(arr[i]>max) max=arr[i];
    
    int gcd = gcd_multi(arr,n);
    
    if((n - (max/gcd)%2 ) % 2 == 0) printf("Bob");
    else printf("Alice");
    
    
    
    return 0;
}
