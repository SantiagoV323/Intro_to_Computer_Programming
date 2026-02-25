# Intro to while loops using press enter to exit

def main():
    print('This program will total all values input AND find the avg')


    num = input('Enter an integer or press enter to quit: ')
    if num == '':
        print('No numbers entered')
        return # the return statement differs from break and else in that break exits the loop and else executes after the loop finishes, while return exits the entire function immediately. In this case, if the user presses enter without entering any numbers, we want to exit the function and not execute the rest of the code that calculates the total and average.

    total = 0 # Initialize the accumulator
    count = 0 # Initialize the counter
    while num != '': #Condition while user does not press enter
        total += int(num) # Accumulate the total
        count += 1 # Increment the counter
        num = input('Enter an integer or press enter to quit: ')
        
    print(f'The total is {total}')
    print(f'The avg is {total / count:.2f}')


main()