class Converter:
    def __init__(self):
        self.priority = {
            '(': 0,
            '+': 1, '-': 1,
            '*': 2, '/': 2,
            '^': 3
        }

    def to_rpn(self, expression):
        stack = []     
        output = []     

        for op in self.priority.keys():
            if op != '(': 
                expression = expression.replace(op, f" {op} ")
        
        expression = expression.replace("(", " ( ").replace(")", " ) ")
        tokens = expression.split()

        for token in tokens:
            if token.replace('.', '', 1).isdigit(): 
                output.append(token)

            elif token == '(':
                stack.append(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack:
                    stack.pop() 

            elif token in self.priority:
                while (stack and stack[-1] != '(' and 
                       self.priority[stack[-1]] >= self.priority[token]):
                    output.append(stack.pop())
                stack.append(token) 

        while stack:
            output.append(stack.pop())

        return output


class Calculator:
    def calculate(self, rpn_list):
        stack = [] 

        for token in rpn_list:
            if token.replace('.', '', 1).isdigit():
                stack.append(float(token))

            else:
                try:
                    b = stack.pop() 
                    a = stack.pop() 
                    
                    res = 0
                    if token == '+': res = a + b
                    elif token == '-': res = a - b
                    elif token == '*': res = a * b
                    elif token == '/': res = a / b
                    elif token == '^': res = a ** b 
                    
                    stack.append(res)
                except IndexError:
                    return "Помилка"

        return stack[0] if stack else 0