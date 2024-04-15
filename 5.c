#include <stdio.h>

// Define macros for factorial calculation
#define FACT_0 1
#define FACT_1 1
#define FACT_2 2
#define FACT_3 6
#define FACT_4 24

// Macro to calculate factorial recursively
#define FACT(n) FACT_##n

// Print factorial of n using recursive-like macros
#define PRINT_FACT(n) printf("Factorial of %d is %d\n", n, FACT(n))

int main() {
    PRINT_FACT(0);
    PRINT_FACT(1);
    PRINT_FACT(2);
    PRINT_FACT(3);
    PRINT_FACT(4);
    
    return 0;
}
