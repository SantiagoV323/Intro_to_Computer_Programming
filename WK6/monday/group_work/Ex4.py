# Write a program that will ask the user for an integer x and then, print the total of x + xx + xxx.
# hint: use concatenation of strings and type cast to an integer
# thest data: input 2, output 246 (2 + 22 + 222)
x = input("Enter an integer: ")
total = int(x) + int(x + x) + int(x + x + x)
print("The total of x + xx + xxx is:", total)