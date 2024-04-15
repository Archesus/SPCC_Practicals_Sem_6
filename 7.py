def generate_mnt_mdt(alp):
    mnt = {}  # Macro Name Table
    mdt = {}  # Macro Definition Table
    macro_name = None
    parameters = []
    inside_macro = False

    for line in alp.split('\n'):
        if line.startswith('MACRO'):
            parts = line.split()
            macro_name = parts[1]
            parameters = parts[2:]
            mnt[macro_name] = len(parameters)
            mdt[macro_name] = []
            inside_macro = True
        elif line.startswith('MEND'):
            inside_macro = False
        elif inside_macro:
            mdt[macro_name].append(line)

    return mnt, mdt

def display_mnt(mnt):
    print("Macro Name Table (MNT):")
    print("Macro Name\t#Parameters")
    for macro, params in mnt.items():
        print(f"{macro}\t\t{params}")

def display_mdt(mdt):
    print("\nMacro Definition Table (MDT):")
    print("Macro Name\tDefinition")
    for macro, definition in mdt.items():
        print(f"{macro}\t\t{' '.join(definition)}")

if __name__ == "__main__":
    alp = """
    MACRO ADD A, B
        MOV A, B
    MEND

    MACRO SUB A, B
        SUB A, B
    MEND
    """

    mnt, mdt = generate_mnt_mdt(alp)
    display_mnt(mnt)
    display_mdt(mdt)
