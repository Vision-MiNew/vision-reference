#include <stdio.h>

int main() {
    int age = 31;
    char name[20] = "MINSOO KIM";  // name[]   []: array   char [] : string

    printf("%s \n", name);          // \n : New line
    printf("%c \n", name[5]); 
    printf("Hello! \t %s \n", name);   // \t : tab 
    printf("Hello! \n %s \t \n", name);           
    printf("Hello! \"%s\" \n", name);       // Hello "MINSOO KIM"

    return 0;
}