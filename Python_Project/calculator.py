def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


if __name__ == "__main__":
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
       
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")
        
     
        if choice == 'q':
            print("Goodbye!")
            break
        

        if choice not in ['1', '2', '3', '4']:
            print("Invalid Input! Please try again.")
            continue
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        print()  # Empty line for better readability 
