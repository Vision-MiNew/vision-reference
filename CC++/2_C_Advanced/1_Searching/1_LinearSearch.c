#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main() {
    int target[] = {23, 45, 72, 53, 92};

    for (int i = 0; i < 5; i++) {
        if(target[i] == 50) {
            printf("Found \n");
            return 0;
        }
    }
    printf("Not Found \n");
    return 1;
}