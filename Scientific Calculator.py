# Scientific Calculator
import math
import time

print("Welcome to the Scientific Calculator!")

def show_list():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Factorial")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Logarithm (Base 10)")
    print("12. Natural Log (ln)")
    print("13. Exponential (e^x)")
    print("14. Exit")

def main():
    while True:
        show_list()
        choice = int(input("Enter your choice (1-14): "))

        if choice in [1, 2, 3, 4]:
            x = int(input("Enter first number:"))
            y = int(input("Enter second number:"))

            if choice == 1:
                print("Result:", x + y)

            elif choice == 2:
                print("Result:", x - y)

            elif choice == 3:
                print("Result:", x * y)

            elif choice == 4:
                if y != 0:
                    print("Result:", x / y)
                else:
                    print("Infinity")

        elif choice == 5:
                x = int(input("Enter a number:"))
                print("Result:", math.sqrt(x))

        elif choice == 6:
                x = int(input("Enter base:"))
                y = int(input("Enter exponent:"))
                print("Result:", math.pow(x,y))

        elif choice == 7:
                x = int(input("Enter a number:"))
                print("Result:", math.factorial(x))

        elif choice == 8:
                x = float(input("Enter an angle:"))
                radian = math.radians(x)
                print("Result:", math.sin(radian))

        elif choice == 9:
                x = float(input("Enter an angle:"))
                radian = math.radians(x)
                print("Result:", math.cos(radian))

        elif choice == 10:
                x = float(input("Enter an angle:"))
                radian = math.radians(x)
                print("Result:", math.tan(radian))

        elif choice == 11:
            x = float(input("Enter a number:"))
            if x > 0:
                    print("Result:", math.log10(x))
            else:
                    print("Error: Logarithm of non-positive number is not defined.")

        elif choice == 12:
            x = float(input("Enter a number:"))
            if x > 0:
                    print("Result:", math.log(x))
            else:
                    print("Error: Natural logarithm of non-positive number is not defined.")
        elif choice == 13:
                x = float(input("Enter a number:"))
                print("Result:", math.exp(x))

        elif choice == 14:
                print("You are exiting the calculator. Goodbye!")  
                break
                
        time.sleep(3)

main()




           
