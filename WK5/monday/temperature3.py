# Intro to if-else and relational operators
# Typically used when testing one specific variable
# if-else is a dual alternative structure - else means ALL other condition
# return 2 T/F values, >=, >, <=, <, !=, ==

def main():

    temp = int(input('Type the temperature'))
    if temp >= 85:
        print("It's hot outside")
    elif temp < 45:
        print("It's nice outside")
    else:
        print("It's nice outside") #Never add a condition to else

main ()