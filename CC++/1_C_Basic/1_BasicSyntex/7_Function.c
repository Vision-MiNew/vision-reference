#include <stdio.h>
#define scanf_s scanf

int test = 8;

float volume_cube(float width, float height, float length) {
    printf("%d", test);
    
    return width * height * length;
}

int main() {
    float width = 0;
    float height = 0;
    float length = 0;
    
    printf("input the cube's width, height, length\n");
    scanf_s("%f %f %f", &width, &height, &length);

    printf("%d", test);
    float volume = 0;
    volume = volume_cube(width, height, length);

    printf("\n\ncube's volume : %f m^3", volume);
    
    return 0;
}