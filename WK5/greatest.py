# Intro t ouse of the boolean operators (and, or, not)

def main():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))

    if num1 >= num2 and num1 >= num3:
        print(f"the greatest number is {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"the greatest number is {num2}")
    else:
        print(f"the greatest number is {num3}")

main()