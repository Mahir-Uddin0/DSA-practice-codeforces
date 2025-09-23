#include<stdio.h>

int main(){
    int t,n,num;
    scanf("%d",&t);
    
    for(int l=0; l<t; l++){
       scanf("%d",&n);
       int a[n], b[n];
       char x[n];
       
       scanf("%s",x);
       
       for(int i=0; i<n; i++){
           num = x[i] - '0';
           
           if(num==2){
               a[i] = 1;
               b[i] = 1;
           }
           else if(num==0){
               a[i] = 0;
               b[i] = 0;
           }
           else if(num==1){
               a[i] = 1;
               b[i] = 0;
               for(int j=i+1; j<n; j++){
                   a[j] = 0;
                   b[j] = x[j] - '0';
               }
               break;
           }
       }
      
      for(int i=0; i<n; i++) printf("%d",a[i]); printf("\n");
      for(int i=0; i<n; i++) printf("%d",b[i]); printf("\n");
    }
    return 0;
}
