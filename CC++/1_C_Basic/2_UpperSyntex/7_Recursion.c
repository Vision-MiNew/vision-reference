#include <stdio.h>

void drawing(int h);

int main() {

    int height =0;

    printf("How many times : ");
    scanf("%d", &height);

    drawing(height);
        
    return 0;
}

void drawing(int h) {

    if (h == 0) {
        return;
    }

    drawing(h-1);

    for (int i = 0; i < h ; i++) {
        printf("#");
    }
    printf("\n");

}