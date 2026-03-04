# example of passing a list
import balance
def calcCommis(sales_list, rate):
    # commis = sum(sales_list) * rate
    # return commis  
    return sum (sales_list) * rate


def main():
    sales = []
    rate = .25
    sale = input('Enter sale or press enter to exit: ')
    while sale != '':
        sales.append(float(sale))
        sale = input('Enter sale or press enter to exit: ')

    print(sales)

    # commission = calcCommis(sales, rate)
    # print(f'Your commission is: {commission:.2f}')
    print(f'Your commission is: {calcCommis(sales, rate):.2f}')    # direct way


main()

balance.bal(100, )