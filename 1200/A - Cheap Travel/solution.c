#include<stdio.h>

int main(){
    int total_ride,m_ride,ticket_price,m_ride_price;
    scanf("%d %d %d %d",&total_ride,&m_ride,&ticket_price,&m_ride_price);
    
    if(m_ride_price/m_ride>=ticket_price) printf("%d",total_ride*ticket_price);
    else{
        if(total_ride%m_ride*ticket_price<m_ride_price) printf("%d",total_ride/m_ride*m_ride_price+total_ride%m_ride*ticket_price);
        else printf("%d",(total_ride/m_ride+1)*m_ride_price);
    }
    return 0;
}
