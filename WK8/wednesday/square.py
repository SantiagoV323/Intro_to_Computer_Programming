# Example of more than 2 functions
import math

def sqrt_(number):
    return math.sqrt(number)

def square(x):
    return x ** 2


def main():
    print('This program determines the square and root of an integer.')
    num = int(input('Enter an integer: '))
    num = square(num)
    print('The square of the number is:', num)
    print('The square root of the number is:', sqrt_(num))




main()