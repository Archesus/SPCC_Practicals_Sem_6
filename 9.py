def optimize_code(code):
    optimized_code = []
    moved_code = []
    loop_variables = set()

    for line in code:
        if "for" in line:
            # Extract loop variable
            loop_var = line.split(" ")[1]
            loop_variables.add(loop_var)
            # Move loop initialization outside loop
            moved_code.append(f"{line.split(':')[0]}:")
            # Check if any statements can be moved outside the loop
            for i in range(len(optimized_code)):
                if loop_var not in optimized_code[i]:
                    moved_code.append(optimized_code[i])
                    optimized_code[i] = ""

        elif any(var in line for var in loop_variables):
            # Move statements that don't depend on loop variables outside loop
            moved_code.append(line)
        else:
            # Store other statements inside loop
            optimized_code.append(line)

    # Add remaining optimized code
    moved_code.extend(optimized_code)

    return moved_code

if __name__ == "__main__":
    # Example code
    code = [
        "for i in range(5):",
        "    x = i + 1",
        "    y = 2 * i",
        "    print(x, y)",
        "    z = x + y",
        "    print(z)",
        "    a = 10",
        "print(a)"
    ]

    print("Original code:")
    for line in code:
        print(line)

    optimized_code = optimize_code(code)

    print("\nOptimized code:")
    for line in optimized_code:
        print(line)
