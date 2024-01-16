#include<stdio.h>
#define max 15
struct process{
    int pid,bt,wt,tt;
};

int main(){
    struct process proc[max],temp;
    int n,i,j;
    int tot_wt=0,tot_tt=0;
    float avg_wt,avg_tt;
    printf("Enter no.of process\n");
    scanf("%d",&n);
    printf("enter process id and brust time\n");
    for(i=0;i<n;i++){
        scanf("%d%d",&proc[i].pid,&proc[i].bt);

    }
    for(i=0;i<n-1;i++){
        for(j=0;i<n-i-1;i++){
            if(proc[j].bt>proc[j+1].bt){
                temp=proc[j];
                proc[j]=proc[j+1];
                proc[j+1]=temp;
            }
        }
    }
    for(i=0;i<n;i++){
        if(i==0){
            proc[0].wt=0;
            proc[0].tt=proc[0].bt;

        }
        else{
            proc[i].wt = proc[i-1].wt + proc[i-1].bt; // waiting time calculation
            tot_wt = tot_wt+proc[i].wt; // total waiting time calculation
            proc[i].tt = proc[i].wt+proc[i].bt ; // turn around time calculation
            tot_tt = tot_tt+proc[i].tt;
        }
    }
    avg_wt = (float) tot_wt/n;
    avg_tt = (float) tot_tt/n;
    printf(" Process ID Burst time Waiting Time Turn Around Time \n");
    for (i = 0; i < n; i++)
        printf(" %d %d %d %d \n", proc[i].pid , proc[i].bt, proc[i].wt, proc[i].tt);
    
    printf("Average waiting time = %f",avg_wt);
    printf("\n");
    printf("Average turn around time = %f ",avg_tt);
}