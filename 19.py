def compute_follow(grammar):
    follow = {non_terminal: set() for non_terminal in grammar.keys()}
    start_symbol = list(grammar.keys())[0]
    follow[start_symbol].add('$')  # Add end of input marker to start symbol FOLLOW set

    while True:
        updated = False
        for non_terminal, productions in grammar.items():
            for production in productions:
                for i, symbol in enumerate(production):
                    if symbol in grammar:
                        if i < len(production) - 1:
                            next_symbol = production[i + 1]
                            if next_symbol in grammar:
                                old_len = len(follow[next_symbol])
                                follow[next_symbol] |= follow[non_terminal]
                                if len(follow[next_symbol]) != old_len:
                                    updated = True
                            else:
                                if 'ε' in follow[non_terminal]:
                                    old_len = len(follow[symbol])
                                    follow[symbol].add('0')  # Represent ε as '0' in FOLLOW set
                                    if len(follow[symbol]) != old_len:
                                        updated = True
                                else:
                                    old_len = len(follow[symbol])
                                    follow[symbol].add(next_symbol)
                                    if len(follow[symbol]) != old_len:
                                        updated = True
                        else:
                            old_len = len(follow[symbol])
                            follow[symbol] |= follow[non_terminal]
                            if len(follow[symbol]) != old_len:
                                updated = True

        if not updated:
            break

    return follow

def get_grammar():
    grammar = {}
    while True:
        non_terminal = input("Enter non-terminal symbol (or leave blank to finish): ")
        if not non_terminal:
            break
        productions = []
        while True:
            production = input(f"Enter production for {non_terminal} (or leave blank to finish): ")
            if not production:
                break
            productions.append(production)
        grammar[non_terminal] = productions
    return grammar

def print_follow_sets(follow):
    print("\nFollow sets:")
    for non_terminal, follow_set in follow.items():
        print(f"Follow({non_terminal}): {' '.join(follow_set)}")

def main():
    print("Enter the grammar:")
    grammar = get_grammar()
    follow = compute_follow(grammar)
    print_follow_sets(follow)

if __name__ == "__main__":
    main()
