#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int x;
void holaMundo (int signalNumber) {
    if(signalNumber == 10){
        printf("Es la señal 10");
        x = 0;
    }else {
        printf("Es otra señal");
    }
}

void noMeMatas(int sig){
    printf("jajaja, no me matas\n");
}

int main () {
    signal(12, holaMundo);
    signal(10, holaMundo);
    signal(2, noMeMatas);

    x = 1;
    while(x == 1){
        printf("Estoy trabajando \n");
        sleep(1);
    }

    printf("Nunca llega \n");
    
    return 0;
}