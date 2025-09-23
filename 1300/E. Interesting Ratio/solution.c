#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

int find_prime(int* prime, int n){
    bool* is_prime = (bool*)malloc((n+1) * sizeof(bool));
    for(int i = 0; i <= n; i++) is_prime[i] = true;
    is_prime[0] = is_prime[1] = false;

    for(int i = 2; i*i <= n; i++){
        if(is_prime[i]){
            for(int j = i*i; j <= n; j += i)
                is_prime[j] = false;
        }
    }

    int length = 0;
    for(int i = 2; i <= n; i++){
        if(is_prime[i]){
            prime[length] = i;
            length++;
        }
    }

    return length;
}

int main(){
    int t, n, size, count, length;
    scanf("%d", &t);

    for(int l = 0; l < t; l++){
        scanf("%d", &n);
        int prime[n];
        length = find_prime(prime, n); 
        int arr[length + 1];

        for(int i = 0; i < length; i++) arr[i] = n / prime[i];
        arr[length] = 0;

        count = 0;
        for(int i = 1; i <= length; i++){
            count += (arr[i - 1] - arr[i]) * i;
        }
        printf("%d\n", count);
    }

    return 0;
}

