#include<stdio.h>
int main(){
    int proc[]={1,2,3};
    int n=3;
    int bt[]={10,5,8};
    int wt[n],tat[n],tot_wt=0,tot_tat=0;
    wt[0]=0;
    for(int i=1;i<n;i++){
        wt[i]=bt[i-1]+wt[i-1];
    }
    for(int i=0;i<n;i++){
        tat[i]=bt[i]+wt[i];
    }
    for(int i=0;i<n;i++){
        tot_wt=tot_wt+wt[i];
        tot_tat=tot_tat+tat[i];
        printf("%d    %d     %d     %d\n",(i+1),bt[i],wt[i],tat[i]);

    }
    int s = (float)tot_wt/n;
    int p = (float)tot_tat/n;
    printf("average wt %d\n",s);
    printf("average tat %d",p);
}