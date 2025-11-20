#include <stdio.h>

void sort(int* arr, int size){
    for(int j=0; j<size-1; j++){
        for(int i=0; i<size-j-1; i++){
            if(arr[i]>arr[i+1]){
                int temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
            }
        }
    }
}

int find_pair(int* arr, int first, int last){
    int count = 1;
    int sum = arr[first] + arr[last];
    first ++; last--;
    while(first<last){
        if(arr[first]+arr[last] == sum){
            count++;
        }
        else if(arr[first]+arr[last]>sum){
            for(int i=last-1; i>first && arr[i]+arr[first]>=sum; i--){
                if(arr[first]+arr[i] == sum){
                    count++;
                    last = i;
                    break;
                }
            }
        }
        else if(arr[first]+arr[last]<sum){
            for(int i=first+1; i<last && arr[i]+arr[last]<=sum; i++){
                if(arr[i]+arr[last] == sum){
                    count++;
                    first = i;
                    break;
                }
            }
        }
        first++;
        last--;
    }
    return count;
}

int main(){
    int t;
    scanf("%d",&t);
    
    while(t>0){
        int n;
        scanf("%d",&n);
        int arr[n];
        for(int i=0; i<n; i++) scanf("%d",&arr[i]);
        sort(arr, n);
        
        int max_count = 0;
        for(int i=0; i<n-1; i++){
            for(int j=n-1; j>i; j--){
                int count = find_pair(arr,i,j);
                if(count > max_count) max_count = count;
            }
        }
        
        printf("%d\n",max_count);
        
        t--;
    }
    
    
    return 0;
}
