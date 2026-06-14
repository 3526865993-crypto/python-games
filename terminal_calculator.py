def main():
    print("===== TERMINAL CALCULATOR =====")
    print("Support: + - * / ( ) and decimal numbers")
    print("Enter 'exit' to quit the program\n")

    while True:
        user_input = input("Please enter calculation: ")
        if user_input.lower() == "exit":
            print("Calculator closed. Goodbye!")
            break
        
        try:
            result = eval(user_input)
            print(f"Result: {result}\n")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed!\n")
        except:
            print("Error: Invalid expression, please try again!\n")

if __name__ == "__main__":
    main()