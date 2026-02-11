# This progam determines the popping time of popcorn

def main():
    print("This program determines the popping time of popcorn")
    ounces = int(input("Enter the number of ounces you want of popcorn: "))
    if ounces < 4:
        print("The popcorn will burn")
    elif ounces > 10:
        print("The popcorn is too much for the microwave")
    else:
        total_seconds = ounces * 50
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        print(f"Pop your popcorn for {minutes:.0f} minutes and {seconds:.0f} seconds")

main()