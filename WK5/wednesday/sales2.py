# Flow of logic for multiple conditions and working with ranges
# 100 or more - 20%
# 50 or more - 15%
# 25 or more - 10%
# 10 or more - 5%

def main():

    price = 1.95
    amount = int(input('Enter the amount of widgets to see your discount and final cost: '))
    
    if amount < 10:
        discount = 1
        print('No discount for you!')
    elif amount < 25:
        discount = 0.05
    elif amount <50:
        discount = 0.1
    elif amount < 100:
        discount = 0.15
    else:
        discount = 0.2
    
    amt_discount = float(amount * discount * price)
    print(f"your discount of {discount*100:.0f}% is ${amt_discount:.2f}, thank you for your purchase")

    total = float(amount * price - amt_discount)
    print(f"Your total is ${total:.2f}")

main()