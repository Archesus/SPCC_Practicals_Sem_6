// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>

// char* convert_instruction(char* instruction) {
//     // Split the instruction into opcode and operands
//     char* opcode;
//     char* operands;
//     char* target_code_instruction;

//     opcode = strtok(instruction, " ");
//     operands = strtok(NULL, "");

//     // Determine the target code instruction based on the intermediate code instruction.
//     if (strcmp(opcode, "ADD") == 0) {
//         asprintf(&target_code_instruction, "add %s", operands);
//     } else if (strcmp(opcode, "SUB") == 0) {
//         asprintf(&target_code_instruction, "sub %s", operands);
//     } else if (strcmp(opcode, "MUL") == 0) {
//         asprintf(&target_code_instruction, "mul %s", operands);
//     } else if (strcmp(opcode, "DIV") == 0) {
//         asprintf(&target_code_instruction, "div %s", operands);
//     } else {
//         // If the opcode is not recognized, return an empty string
//         target_code_instruction = strdup("");
//     }

//     return target_code_instruction;
// }

// char** generate_target_code(char** intermediate_code, int num_instructions) {
//     char** target_code = (char**)malloc(num_instructions * sizeof(char*));
//     for (int i = 0; i < num_instructions; i++) {
//         // Convert the intermediate code instruction to a target code instruction.
//         target_code[i] = convert_instruction(intermediate_code[i]);
//     }
//     return target_code;
// }

// int main() {
//     // Example usage:
//     char* intermediate_code[] = {"ADD eax, ebx", "SUB eax, ebx", "MUL eax, ebx", "DIV eax, ebx"};
//     int num_instructions = sizeof(intermediate_code) / sizeof(intermediate_code[0]);

//     char** target_code = generate_target_code(intermediate_code, num_instructions);

//     // Print the generated target code
//     for (int i = 0; i < num_instructions; i++) {
//         printf("%s\n", target_code[i]);
//         free(target_code[i]); // Free dynamically allocated memory
//     }

//     free(target_code);

//     return 0;
// }
