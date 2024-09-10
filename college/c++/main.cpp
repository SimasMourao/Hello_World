/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
/*AULA 09/09/24*/

#include <stdio.h>

int main()
{
    int a = 0, b = 0;
    printf("digite um n:");
    scanf("%d", &a);
    printf("\ndigite um outro n:");
    scanf("%d", &b);
    if (a > b)
    {
        printf("\n%d e maior que %d\n", a, b);
    }
    if (a < b)
    {
        printf("\n%d e maior que %d\n", b, a);
    }
    if (a == b)
    {
        printf("\nos dois numeros sao iguaus\n");   
    }
    printf("\na soma dos numeros e: %d", a+b);
    return 0;
}
