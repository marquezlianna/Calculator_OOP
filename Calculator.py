# create a class named Calculator
class Calculator:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.operation = None
        self.ans = None
     
     # Ask the user to enter a number   
    def get_input(self):
        print("\n")
        try:
            self.num1 = float(input("Please enter your first number: "))
            self.num2 = float(input("Please enter your second number: "))
        except ValueError as error:
            print("Invalid number input\n")
            print(error)
            print("\nTry Again!")
            return False
        return True
    
    # Ask user to choose operation
    def get_operation(self):
        self.operation = input("Please enter an operation: +-*/ ")
     
    