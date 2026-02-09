# intro to logic used to compare multiple variables
def main():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))

    max = num1
    if max < num2:
        max = num2
    if max < num3:
        max = num3
    print(f"The greatest number is {max}")

main()