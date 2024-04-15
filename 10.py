def build_symbol_table(alp):
    symbol_table = {}
    current_address = 0

    for line in alp.split('\n'):
        if line.strip():
            parts = line.split()
            label = parts[0].strip(':')
            if label:  # If line has a label
                symbol_table[label] = current_address
            current_address += 1

    return symbol_table

def display_symbol_table(symbol_table):
    print("Symbol Table:")
    print("Label\tAddress")
    for label, address in symbol_table.items():
        print(f"{label}\t{address}")

if __name__ == "__main__":
    alp = """
    START:  MOV A, 5
            INC A
    LOOP:   DEC A
            JNZ LOOP
            HLT
    """

    symbol_table = build_symbol_table(alp)
    display_symbol_table(symbol_table)
