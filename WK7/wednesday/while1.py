# Intro to while loops using accumulator and counter
# Initialization, condition and update
# While loops are used when we don't know how many times we need to repeat a block of code

def main():
    print('This program will total all values input AND find the avg')

    num = int(input('Enter an integer or 0 to quit: '))
    total = 0 # Initialize the accumulator
    count = 0 # Initialize the counter
    while num > 0:
        total += num # Accumulate the total
        count += 1 # Increment the counter
        num = int(input('Enter an integer or 0 to quit: '))
    print(f'The total is {total}')
    print(f'The avg is {total / count:.2f}')


main()