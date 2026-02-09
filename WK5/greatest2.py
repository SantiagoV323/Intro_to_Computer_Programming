# Intro t ouse of the nested if statements
# please do not use nume1 >= num2 >= num3, it will not work, you need to use the boolean operators (and, or, not)

def main():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))

    if num1 >= num2:
        if num1 >= num3:
            print(f"the greatest number is {num1}")
        else:
            print(f"the greatest number is {num3}")
    else:
        if num2 >= num3:
            print(f"the greatest number is {num2}")
        else:
            print(f"the greatest number is {num3}")

main()