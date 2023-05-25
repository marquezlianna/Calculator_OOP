from Calculator import Calculator
from user_interface import UserInterface

def main():
    calculator = Calculator()
    user_interface = UserInterface(calculator)
    user_interface.run()

if __name__ == "__main__":
    main()