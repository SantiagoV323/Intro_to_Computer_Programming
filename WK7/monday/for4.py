# Counted for loop editing a list

def main():
    
    myList = [5, 10, 15, 20, 25, 30, 35]
    # In order to change content of a list, you must use subscript notation
    for i in range(len(myList)): #Use range to generate index values
        myList[i] += 2  # In this line, i accesses the index value of the list, and the += operator adds 2 to the value at that index

    for num in myList:
        print(num)


main()