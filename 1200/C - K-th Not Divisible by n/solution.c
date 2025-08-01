#include<stdio.h>

int main(){
    int t;
    scanf("%d",&t);
    int n[t],k[t];
    for(int i=0; i<t; i++) scanf("%d %d",&n[i],&k[i]);
    
    for(int i=0; i<t; i++){
        if(k[i]%(n[i]-1)==0) printf("%d\n",k[i]/(n[i]-1)*n[i]+k[i]%(n[i]-1)-1);
        else printf("%d\n",k[i]/(n[i]-1)*n[i]+k[i]%(n[i]-1));
    }
    return 0;
}
