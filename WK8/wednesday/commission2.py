# Example of using the return value of one function pass to another function

# example of passing a list

def net_pay (commis, tax_rate):
    net = commis - commis * tax_rate
    return net


def calcCommis (sales_list, rate):
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

    commission = calcCommis(sales, rate)
    print(f'Your gross commission is: {commission:.2f}')
    
    net = net_pay(commission, tax=0.1)
    print(f'Your net pay is: {net:.2f}')

main()