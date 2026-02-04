# Example of a string list
# Use of the .append() method, .remove() method and pop() method 

def main():
    mylist = ['flour', 'eggs', 'milk']  # Create a list of strings
    print("Initial list:", mylist)
    mylist.append('chocolate')  # Add an item to the end of the list
    print("After appending 'chocolate':", mylist)
    mylist.remove('eggs')  # Remove a specific item from the list
    print("After removing 'eggs':", mylist)
    mylist.pop(0)  # Remove the first item from the list
    print("After popping the first item:", mylist)
    myset = set(mylist)  # Convert the list to a set to remove duplicates
    print("Converted to set (duplicates removed):", myset)

main()