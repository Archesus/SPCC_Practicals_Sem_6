class RecursiveDescentParser:
    def __init__(self, expression):
        self.expression = expression
        self.index = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        result = self.parse_term()
        while self.index < len(self.expression):
            op = self.expression[self.index]
            if op in ('+', '-'):
                self.index += 1
                term = self.parse_term()
                result += term if op == '+' else -term
            else:
                break
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.index < len(self.expression):
            op = self.expression[self.index]
            if op in ('*', '/'):
                self.index += 1
                factor = self.parse_factor()
                result *= factor if op == '*' else 1 / factor
            else:
                break
        return result

    def parse_factor(self):
        if self.expression[self.index].isdigit():
            return self.parse_number()
        elif self.expression[self.index] == '(':
            self.index += 1
            result = self.parse_expression()
            self.index += 1
            return result

    def parse_number(self):
        number = ""
        while self.index < len(self.expression) and self.expression[self.index].isdigit():
            number += self.expression[self.index]
            self.index += 1
        return int(number)

# Test the parser
expression = "3 + 4 * (5 - 2)"
parser = RecursiveDescentParser(expression)
result = parser.parse()
print("Result:", result)
