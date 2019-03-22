class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        item = self.s.pop()
        return item

def rpn(tokens):
    s = Stack()
    ops = ['+', '-', '/', '*']
    tokens = tokens.split()
    
    for token in tokens:
        if token not in ops:
            s.push(int(token))
        else:
            op1 = s.pop()
            op2 = s.pop()
            
            if token == '+':
                s.push(op1 + op2)
            elif token == '-':
                s.push(op2 - op1)
            elif token == '*':
                s.push(op2 * op1)
            else:
                s.push(int(op2 / op1))
                
    return s.pop()

tokens = '1000 990 1 2 + * +'
rpn(tokens)
