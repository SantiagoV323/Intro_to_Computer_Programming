# Correct this program
# Test data: 9.5 gallons and 33 miles = 34.7 mpg

def main ():
    print("This program calculates miles per gallon")
    gallons = float(input("Please write the gallons: "))
    miles = float(input("Please write the miles: "))
    print(f"Miles per gallon: {(miles / gallons):.2f}")

main()