#include <stdio.h>
#include <string.h>

void remove_dead_code(char *code) {
    char *token;
    char *delimiters = ";\n";
    char *dead_code_markers[] = {"UNUSED", "TODO", "FIXME"};
    int i;

    // Tokenize the code based on delimiters
    token = strtok(code, delimiters);
    while (token != NULL) {
        int is_dead_code = 0;

        // Check if the token contains any dead code markers
        for (i = 0; i < sizeof(dead_code_markers) / sizeof(dead_code_markers[0]); i++) {
            if (strstr(token, dead_code_markers[i]) != NULL) {
                is_dead_code = 1;
                break;
            }
        }

        // If it's not dead code, print it
        if (!is_dead_code) {
            printf("%s;\n", token);
        }

        token = strtok(NULL, delimiters);
    }
}

int main() {
    char code[] = "int x = 5; // UNUSED variable\n"
                  "int y = 10;\n"
                  "int z = x + y; // FIXME: Possible overflow\n"
                  "printf(\"Result: %d\\n\", z);\n"
                  "// TODO: Add more functionality\n";

    printf("Original code:\n");
    printf("%s\n", code);

    printf("\nCode after dead code elimination:\n");
    remove_dead_code(code);

    return 0;
}
