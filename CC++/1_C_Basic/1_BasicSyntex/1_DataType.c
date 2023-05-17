#include <stdio.h>  // standard Input/Putput

// Declaration "Main" Function   () -> function
int main() {
    // Character - letter/number(can not calcurate)
    char s = 'a';               // c
    unsigned char cha = 'g';    // uc

    // Integer - Natural Numbers     size of short : half int       size of long : double int
    int x = 0;                  // d
    short sx = 3;               // d
    long lx = 3;                // d
    unsigned int ux = 3;        // ud
    unsigned short usx = 3;     // ud
    unsigned long ulx = 3;      // ud

    // Float - Real Numbers     size of double : double of float
    float y = 3.2;              // f
    double dy = 3.2;            // f

    printf("%c \n", s);
    printf("%d \n", sizeof(s));
    printf("%c \n", cha);
    printf("%d \n", sizeof(cha));
    printf("%d \n", x);
    printf("%d \n", sizeof(x));    
    printf("%d \n", sx);
    printf("%d \n", sizeof(sx));
    printf("%d \n", lx);
    printf("%d \n", sizeof(lx));
    printf("%d \n", ux);
    printf("%d \n", sizeof(ux));
    printf("%d \n", sx);
    printf("%d \n", sizeof(sx));
    printf("%d \n", ulx);
    printf("%d \n", sizeof(ulx));
    printf("%f \n", y);
    printf("%d \n", sizeof(y));
    printf("%f \n", dy);
    printf("%d \n", sizeof(dy));

    return 0;
}