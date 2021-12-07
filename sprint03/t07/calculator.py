operation = {"add": lambda n1,n2: n1+n2,
             "sub": lambda n1,n2: n1-n2,
             "mul": lambda n1,n2: n1*n2,
             "div": lambda n1,n2: n1/n2,
             "pow": lambda n1,n2: n1**n2
            }

def calculator(oper, a, b):
    if oper not in operation:
        raise ValueError('Invalid operation. Available operations: add, sub, mul, div, pow.')
    elif not isinstance(a,(int,float)) and not isinstance(b,(int,float)):
        raise ValueError('Invalid numbers. Second and third arguments must be numerical.')
    else:
        return  operation[oper](a,b)


# print(calculator('pow', 2, 3))