#include <stdio.h>
int n, total=0;

int combination(int *arr, int start, int c, int sum){
    if(c==0) return 0;
    for(int i=start; i<n; i++){
        sum+= arr[i];
        if((total-2*sum)%360==0) return 1;
        if(combination(arr,i+1,c-1,sum)) return 1;
        sum-=arr[i];
    }
    return 0;
}

int main(){
    int result = 0;
    scanf("%d",&n);
    int arr[n];
    for(int i=0; i<n; i++){
        scanf("%d",&arr[i]);
        total+=arr[i];
    }
    printf("\n\n");
    if(total%360==0 || combination(arr,0,n/2,0)) printf("YES");
    else printf("NO");

    return 0;
}
