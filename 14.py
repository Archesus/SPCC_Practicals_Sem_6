temp_count = 0

def new_temp():
    global temp_count
    temp = "t" + str(temp_count)
    temp_count += 1
    return temp

def generate_three_address_code(op, arg1, arg2, result):
    print(f"{result} = {arg1} {op} {arg2}")

def main():
    expr = input("Enter an arithmetic expression (e.g., a + b * c - d): ")
    tokens = expr.split()
    temp1 = tokens[0]
    temp2 = None
    op = None

    for token in tokens[1:]:
        if token in "+-*/":
            op = token
        else:
            temp2 = token
            result = new_temp()
            generate_three_address_code(op, temp1, temp2, result)
            temp1 = result

    if temp2:
        del temp1, temp2

if __name__ == "__main__":
    main()
