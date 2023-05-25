class UserInterface:
    def __init__(self, Calculator):
        self.calculator = Calculator
        
    def run(self):
        while True:
            # ask user for the input number
            if not self.calculator.get_input():
                continue
            # ask user to input operation
            self.calculator.get_operation()
            # perform the operation
            if not self.calculator.perform_operation():
                continue
            # print output
            self.calculator.print_output()
            # ask user to try again
            print("\n")
            try_again = input('\033[1;34m'f"Do you want to try again? (yes/no): ")
            if try_again.lower() != "yes":
                print('\033[1;95;40m'f"Thank you for using the Simple Calculator App!")
                break