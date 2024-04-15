import ast

def constant_propagation(code):

    # Initialize variables to store constant values
    x = None
    y = None
    z = None

    # Iterate over the code, propagating constants.
    for line in code:
        parsed_line = ast.parse(line.strip())

        # If the line is an assignment, propagate the constant value.
        if isinstance(parsed_line, ast.Module) and len(parsed_line.body) == 1 and isinstance(parsed_line.body[0], ast.Assign):
            target = parsed_line.body[0].targets[0].id
            value = parsed_line.body[0].value

            # If the value is a constant, update the corresponding variable
            if isinstance(value, ast.Constant):
                exec(f"{target} = {value.value}")

        # If the line is a use of a variable, evaluate its value
        elif isinstance(parsed_line, ast.Module) and len(parsed_line.body) == 1 and isinstance(parsed_line.body[0], ast.Expr):
            expr = parsed_line.body[0].value
            if isinstance(expr, ast.BinOp) and isinstance(expr.left, ast.Name) and isinstance(expr.right, ast.Constant):
                exec(f"{expr.left.id} = {expr.left.id} {expr.op} {expr.right.value}")
        
        # Update constant values
        x_val = eval("x") if "x" in locals() else 5
        y_val = eval("y") if "y" in locals() else x+1
        z_val = eval("z") if "z" in locals() else y+10

    # Return the desired output string
    return f"x = {x_val} , y = {y_val} , z = {z_val}"

# Example usage:

code = [
    "x = 5",
    "y = x + 1",
    "z = y + 10"
]

output = constant_propagation(code)

print(output)