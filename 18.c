#include <stdio.h>

// Define conditional macros
#define DEBUG

#ifdef DEBUG
    #define DEBUG_PRINT(x) printf("Debug: %s\n", x)
#else
    #define DEBUG_PRINT(x) do {} while (0)
#endif

int main() {
    int x = 10;

    // Conditional debug print
    DEBUG_PRINT("This is a debug message");

    // Normal print
    printf("Value of x: %d\n", x);

    return 0;
}
