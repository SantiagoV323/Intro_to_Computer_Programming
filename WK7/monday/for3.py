# Counted for loop summing up a list

def main():
    
    myList = [5, 10, 15, 20, 25, 30, 35]
    sum = 0
    for num in myList:
        sum += num
    print(f"Sum: {sum}")
    print(f"Average: {sum / len(myList)}")

main()