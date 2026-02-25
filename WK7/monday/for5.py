# Counted for loop summing up a list but data entered through the keyboard

def main():
    myList = []
    numint = int(input("How many integers would you like to enter? "))

    # Input validation to ensure a positive integer is entered for the number of integers
    if numint <= 0:
        print("Please enter a positive integer.")
        return
    
    # The loop will run numint times, allowing the user to enter the specified number of integers
    # x is used to keep track of the current iteration, starting from 0. 
    # The input prompt will display the current integer number (x+1) to guide the user.
    for x in range(numint):
        num = int(input(f'Please enter an integer #{x+1}: '))
        myList.append(num)
    
    print(f"Sum of the list: {sum(myList)}")
    print(f"Average of the list: {sum(myList) / len(myList)}")

main()