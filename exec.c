#include <stdio.h>
#include <unistd.h>
int main() {
    printf("Prueba\n");
    int pid = fork();
    
    if (pid == 0) {
        printf("Soy el proceso hijo y me voy a convertir en ls\n");
        execl("/workspace/IoT-Tec-TC1004B.513/hola", "hola", NULL);
        printf("Esto no debe de ejecutarse");
    } else {
        printf("Soy el proceso padre \n");
     
    }
    
    return 0;

}