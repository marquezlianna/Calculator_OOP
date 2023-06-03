from Calculator import Calculator
from user_interface import UserInterface
from inherited_calculator import InheritedCalculator

def main():
    calculator = Calculator()
    user_interface = UserInterface(calculator)
    inherited_calculator = InheritedCalculator()
    user_interface.run()
    inherited_calculator()
    
if __name__ == "__main__":
    main()
