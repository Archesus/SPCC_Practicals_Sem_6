def generate_quadruples(expression):
    quadruples = []

    parts = expression.split('+')
    temp_var1 = parts[1]
    quadruples.append(f"T1 = {parts[1]}")
    quadruples.append(f"T2 = {parts[0]} + T1")
    quadruples.append(f"T3 = T2 + {parts[2]}")

    return quadruples

# Example usage
if __name__ == "__main__":
    expression = "a+b*c+d"
    quadruples = generate_quadruples(expression)
    for q in quadruples:
        print(q)