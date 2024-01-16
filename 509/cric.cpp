#include<bits/stdc++.h>
using namespace std;
class cric
{
    string team1[11];
    string team2[11];
    int n;
    string team[2];
    public:
    void toss()
    {
        cout<<"who won the toss\n";
        cout<<"1.\n2.%s\n",team[1],team[2];
        cin>>n;
        if(n=1)
        cout<<team[1]<<" won the toss and choose to bat\n";
        else
        cout<<team[2]<<" won the toss and choose to bat\n";
    }
    void getteam()
    {
        cout<<"enter team name\n";
        cin>>team[1];
        cout<<"Enter %s team A members details\n",team[1];
        for(int i=0;i<11;i++)
        {
            cin>>team1[i];
        }
        cout<<"Enter team name\n";
        cin>>team[2];
        cout<<"Enter team B details\n",team[2];
        for(int i=0;i<11;i++)
        {
            cin>>team1[i];
        }
    }
    void intialse()
    {
        
    }


};
int main()
{
    cric ob;
    ob.getteam();
    ob.toss();
    

}