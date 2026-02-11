# use of relational operators with strings

def main():
    first = input("Enter the first friend's name: ")
    second = input("Enter the second friend's name: ")

    if first > second:
        print(f"{first} is the greatest")
    else:
        print(f"{second} is the greatest")

main()