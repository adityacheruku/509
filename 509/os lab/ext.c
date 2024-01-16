#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
#define buff_s 1000
int main(){
    int n, fd1, fd2;
    char buf[buff_s];
    fd1 = open("text.txt",O_RDONLY,0644);
    n = read(fd1,buf,buff_s);
    fd2 = oen("txt2.txt",O_CREAT|O_RDWR,0777);
    if(write(fd2,buf,n)==n){
        printf("success");
    }
    write(1,buff,n);
    int close(fd1);
    int close(fd2);
    
    return 0;
}