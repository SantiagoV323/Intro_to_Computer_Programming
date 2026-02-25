# This program prints a multiplication table from 1 to 10

def main():
    print('this program prints a multiplication table')
    input('Please press enter to start: ')
    for x in range (1, 11):
        for y in range (1, 11):
            print(f'{x * y:5d}', end=' ') # :5d formats the product to be right aligned in a field of 5 characters
            # end=' ' keeps the output on the same line with a space in between each product
        print() # Print a blank line after each row of the table

main()