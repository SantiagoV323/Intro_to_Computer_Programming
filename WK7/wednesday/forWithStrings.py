# Using a list of stings

def main():
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for i in weekdays:
        print(f'{i:10s}', end=' ') # :10s formats the string to be left aligned in a field of 10 characters
    print() # Print a blank line after the loop 

    # This block of code does the same as the above block but uses an index to access each element in the list
    # Basically every weekday is stored in a list and has an index that starts at 0 and goes to 6.
    
    ''' The for loop iterates through the range of the length of the list (which is 7) and uses 
    the index to access each element in the list and print it formatted to be left aligned in a field of 10 characters
    with a space in between each element. After the loop, a blank line is printed.'''

    print('\n\n') # Print two blank lines to separate the output of the two loops
    for i in range(len(weekdays)):
        print(f'{weekdays[i]:10s}', end=' ')


    # This block of code does the same as the above block but also prints the index of each element in the list
    print('\n\n')  # Print two blank lines to separate the output of the two loops
    for i in range(len(weekdays)):
        print(f'Day # {i + 1} = {weekdays[i]}')

main()