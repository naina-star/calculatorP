from calculator import Calculator
from config import CalculatorConfig
from history import History

def main():
    # Load configurations and create instances of the calculator and history manager.
    config = CalculatorConfig()
    calc = Calculator(precision=config.precision)
    history = History(max_size=config.max_history_size, auto_save=config.auto_save, base_dir=config.base_dir)

    print("Welcome to the calculator!")

    # REPL loop: keep asking the user for commands until they want to quit.
    while True:
        print("Commands: add, subtract, multiply, divide, power, root, history, clear, exit")
        command = input("Enter command: ").strip().lower()

        if command == "exit":
            # Exit the calculator when the user types "exit".
            print("Goodbye!")
            break

        if command == "history":
            # Display the calculation history.
            print("Calculation History:")
            for entry in history.history:
                print(entry)

        elif command == "clear":
            # Clear the calculation history.
            history.clear_history()
            print("History cleared.")

        else:
            # For all other commands, ask the user for two operands.
            try:
                operands = input("Enter two operands separated by space: ").split()
                a, b = map(float, operands)  # Convert the operands to floats.

                # Perform the requested operation and print the result.
                if command == "add":
                    result = calc.add(a, b)
                elif command == "subtract":
                    result = calc.subtract(a, b)
                elif command == "multiply":
                    result = calc.multiply(a, b)
                elif command == "divide":
                    result = calc.divide(a, b)
                elif command == "power":
                    result = calc.power(a, b)
                elif command == "root":
                    result = calc.root(a, b)
                else:
                    print("Unknown command. Try again.")
                    continue

                print(f"Result: {result}")
                history.add(f"{command}({a}, {b}) = {result}")

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the calculator application when this script is executed.
    main()
