#include <stdio.h>
#include <string.h>

// Structure to represent an expression
typedef struct {
    char *expression;
    char *result;
} Expression;

// Function to perform common subexpression elimination
void eliminate_common_subexpressions(Expression *expressions, int num_expressions) {
    int i, j;

    // Compare each pair of expressions
    for (i = 0; i < num_expressions; i++) {
        for (j = i + 1; j < num_expressions; j++) {
            // If both expressions are identical, replace the second one with a reference to the first one
            if (strcmp(expressions[i].expression, expressions[j].expression) == 0) {
                expressions[j].result = expressions[i].result;
            }
        }
    }
}

// Function to display expressions after common subexpression elimination
void display_expressions(Expression *expressions, int num_expressions) {
    printf("Expressions after Common Subexpression Elimination:\n");
    for (int i = 0; i < num_expressions; i++) {
        printf("%s = %s\n", expressions[i].result, expressions[i].expression);
    }
}

int main() {
    // Array of expressions
    Expression expressions[] = {
        {"x + y", "temp1"},
        {"x + y", "temp2"},
        {"x * 2", "temp3"},
        {"x * 2", "temp4"},
        {"x + z", "temp5"},
    };

    int num_expressions = sizeof(expressions) / sizeof(expressions[0]);

    printf("Expressions before Common Subexpression Elimination:\n");
    for (int i = 0; i < num_expressions; i++) {
        printf("%s = %s\n", expressions[i].result, expressions[i].expression);
    }

    // Perform common subexpression elimination
    eliminate_common_subexpressions(expressions, num_expressions);

    // Display expressions after common subexpression elimination
    display_expressions(expressions, num_expressions);

    return 0;
}
