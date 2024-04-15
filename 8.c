#include <stdio.h>

// Define a parameterized macro for finding the maximum of two numbers
#define MAX(a, b) ((a) > (b) ? (a) : (b))

// Define a parameterized macro for swapping two numbers
#define SWAP(x, y) do { \
                        typeof(x) temp = (x); \
                        (x) = (y); \
                        (y) = temp; \
                    } while (0)

int main() {
    int x = 5, y = 10;
    printf("Maximum of %d and %d is %d\n", x, y, MAX(x, y));

    printf("Before swap: x = %d, y = %d\n", x, y);
    SWAP(x, y);
    printf("After swap: x = %d, y = %d\n", x, y);

    return 0;
}
