import sympy as sp
x = sp.symbols('x')

def operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Division by zero")
    else:
        raise ValueError("Invalid operator")
def calculator(l):

    i = 0
    while i < len(l):
        if l[i] in ('*', '/'):
            left = float(l[i-1])
            right = float(l[i+1])
            result = operation(left, right, l[i])
            l[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1
    
    result = float(l[0])
    i = 1
    while i < len(l):
        op = l[i]
        num = float(l[i+1])
        result = operation(result, num, op)
        i += 2
    
    return result

print("0. Basic Calculation")
print("1. Differentiation")
print("2. Integration")
choice = input("Enter choice (0/1/2): ")

if (choice=='1' or choice=='2'):
    expression = input("Enter function in terms of x: ")
    expr = sp.sympify(expression)
    if choice == '1':
        result = sp.diff(expr, x)
        print(result)
    elif choice == '2':
        result = sp.integrate(expr, x)
        print(result)

elif (choice == '0'):
    a = input()
    l = a.split()
    print("Result:", calculator(l))