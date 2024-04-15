# 1)WAP to generate the target code for X86 , given the intermediate code.



def generate_target_code(intermediate_code):
    """Generates the target code for X86, given the intermediate code.

    Args:
      intermediate_code: A list of intermediate code instructions.

    Returns:
      A list of target code instructions.
    """

    target_code = []
    for instruction in intermediate_code:
        # Convert the intermediate code instruction to a target code instruction.
        target_code_instruction = convert_instruction(instruction)

        # Add the target code instruction to the list of target code instructions.
        target_code.append(target_code_instruction)

    return target_code


def convert_instruction(instruction):
    """Converts the intermediate code instruction to a target code instruction.

    Args:
      instruction: An intermediate code instruction.

    Returns:
      A target code instruction.
    """

    # Split the instruction into opcode and operands
    parts = instruction.split()
    opcode = parts[0]
    operands = parts[1:]

    # Determine the target code instruction based on the intermediate code instruction.
    if opcode == "ADD":
        target_code_instruction = "add " + ", ".join(operands)
    elif opcode == "SUB":
        target_code_instruction = "sub " + ", ".join(operands)
    elif opcode == "MUL":
        target_code_instruction = "mul " + ", ".join(operands)
    elif opcode == "DIV":
        target_code_instruction = "div " + ", ".join(operands)
    else:
        # If the opcode is not recognized, return an empty string
        target_code_instruction = ""

    return target_code_instruction


# Example usage:

intermediate_code = ["ADD eax, ebx", "SUB eax, ebx", "MUL eax, ebx", "DIV eax, ebx"]
target_code = generate_target_code(intermediate_code)

print(target_code)