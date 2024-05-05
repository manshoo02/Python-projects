def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1- n2

def divide(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2

operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
    }

def calculator():
    num1 = float(input("Enter the first number : "))
    for symbol in operations:
        print(symbol)
        
    cont = True
    
    while cont:
        op_symbol = input("Pick an operation : ")
        if op_symbol not in ["+", "-" , "/","*"]:
            print("Invalid operator!")
            op_symbol = input("Pick an operation : ")

        num2 = float(input("Enter the next number : "))
        calc_function = operations[op_symbol]
        ans = calc_function(num1,num2)
        
        print(f"{num1} {op_symbol} {num2} = {ans}")
        
        temp = input("Type 'y' to continue an operation with the answer , 'n' to start a new calculation and 'e' to exit the calculator program : ").lower()
        if temp == "y":
            num1 = ans
        elif temp == "n":
            cont = False
            calculator()
        elif temp == "e":
            cont = False
            print("Thanks for using the calculator program!")
        else:
            print("Invalid input! Read the instruction carefully")
            temp = input("Type 'y' to continue an operation with the answer , 'n' to start a new calculation and 'e' to exit the calculator program").lower()
            
        
calculator()   