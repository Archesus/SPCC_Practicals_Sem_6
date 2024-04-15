def find_first(grammar):
    first = {}
    for non_terminal in grammar.keys():
        first[non_terminal] = set()

    changed = True
    while changed:
        changed = False
        for non_terminal, productions in grammar.items():
            for production in productions:
                for symbol in production:
                    if symbol in grammar.keys():
                        initial_length = len(first[non_terminal])
                        first[non_terminal] |= first[symbol]
                        if len(first[non_terminal]) != initial_length:
                            changed = True
                        if '' not in first[symbol]:
                            break
                    else:
                        initial_length = len(first[non_terminal])
                        first[non_terminal].add(symbol)
                        if len(first[non_terminal]) != initial_length:
                            changed = True
                        break
                else:
                    first[non_terminal].add('')
    return first

def display_first(first):
    print("FIRST sets:")
    for non_terminal, symbols in first.items():
        print(f"FIRST({non_terminal}) = {symbols}")

if __name__ == "__main__":
    # Example grammar
    grammar = {
        'S': ['AB', 'BC'],
        'A': ['a', ''],
        'B': ['b', ''],
        'C': ['c']
    }

    first = find_first(grammar)
    display_first(first)
