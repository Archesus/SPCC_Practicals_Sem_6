#include <stdio.h>

#define SQUARE(x) ((x) * (x))
#define CUBE(x) (SQUARE(x) * (x))

int main() {
    int num = 5;
    printf("Square of %d is %d\n", num, SQUARE(num));
    printf("Cube of %d is %d\n", num, CUBE(num));
    return 0;
}