# More than one parameter and no specific value returned

def bal(dep, rate, yrs):
    for x in range(yrs):
        dep = dep + (dep * rate)
    return dep

def main():
    print('This program calculates interest and ending balance for an investment')
    dep = float(input('Enter the initial deposit: '))
    rate = float(input('Enter the interest rate Ex: 0.05 for 5%: '))
    years = int(input('Enter the number of years: '))
    total = bal(dep, rate, years) #arguments must match the parameter list
    # in type, order, and number 
    print ()