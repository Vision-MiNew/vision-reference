#include <stdio.h>

float add(num1, num2) {
    return num1+num2;
}

int main() {
    int result = 5;
    double x = 5;

    printf("result : ");

    printf("%zu \n", sizeof(result)); // zu => Byte
    // result라는 variable을 위해서 메모리에 얼마나 공간을 사용하였는지 알려줘.
    // -> 4 byte was allocated for 'Result' variable.
    printf("%zu \n", sizeof(x));
    return 0;
}