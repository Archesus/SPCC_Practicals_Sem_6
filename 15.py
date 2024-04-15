def remove_left_recursion(grammar):
    new_grammar = {}
    for A, productions in grammar.items():
        non_recursive = [prod for prod in productions if prod[0] != A]
        recursive = [prod[1:] for prod in productions if prod[0] == A]
        if not recursive:
            new_grammar[A] = productions
            continue
        A_prime = A + "'"
        new_grammar[A] = [prod + A_prime for prod in non_recursive] + ['b' + A_prime]
        new_grammar[A_prime] = ['aB' + A_prime, 'ε']
    return new_grammar

def get_grammar():
    grammar = {}
    while True:
        non_terminal = input("Non-terminal symbol (blank to finish): ")
        if not non_terminal: break
        productions = []
        while True:
            production = input(f"Production for {non_terminal} (blank to finish): ")
            if not production: break
            productions.append(production)
        grammar[non_terminal] = productions
    return grammar

def print_grammar(grammar):
    print("\nGrammar:")
    for non_terminal, productions in grammar.items():
        print(non_terminal + ' -> ' + ' | '.join(productions))

def main():
    print("Enter the grammar:")
    grammar = get_grammar()
    print_grammar(grammar)
    new_grammar = remove_left_recursion(grammar)
    print("\nGrammar after Left Recursion Removal:")
    print_grammar(new_grammar)

if __name__ == "__main__":
    main()
