# Flow of logic for multiple conditions and working with ranges
# 100 or more - 20%
# 50 or more - 15%
# 25 or more - 10%
# 10 or more - 5%

def main():

    amount = int(input('Enter the amount of widgets to see your discount: '))
    
    if amount < 10:
        print('No discount for you!')
    elif amount < 25:
        print('Discount is 5%')
    elif amount <50:
        print('Discount is 10%')
    elif amount < 100:
        print('Discount is 15%')
    else:
        print('Discount is 20%')

    print("Thank you for your purchase")

main()