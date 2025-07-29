#include<stdio.h>

 int main(){
     int size;
     scanf("%d",&size);
     int p_3[size], p_4[size],p[size];
     
     for(int i=0; i<size; i++){
         scanf("%d",&p_3[i]);
     }
     for(int i=0; i<size; i++){
         scanf("%d",&p_4[i]);
     }
     
     for(int i=0; i<size; i++){
         p[p_3[i]-1] = p_4[i];
     }
     
     for(int i=0; i<size; i++){
         printf("%d ",p[i]);
     }
     
     return 0;
 }
