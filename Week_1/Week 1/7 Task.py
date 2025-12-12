a = float(input("First number: "))
operation = input("Operation (+ - * /): ")
b = float(input("Your second number: "))
if operation == "/":
    print(a / b if b != 0 else "Error: division by zero")