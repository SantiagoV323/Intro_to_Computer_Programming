# Correct this program that totals sale and tax
# Instead of using sale_amt, ask the user to enter number of items purchased and price. Then calculate
# Test: 20 items at 1.95 per item = 39.00 + 3.80 tax = $42.80

def sale():
    sale_amt = int(input("Please enter the amount of items: "))
    price = float(input("Please enter the price: "))
    tax = 9.75369
    sales_person = "Julie" #String

    print("This program determines the total sale plus tax ")
    total_sale = (sale_amt * price) * (1 + tax / 100)
    print(f"The total sale is: ${total_sale:.2f}")
    print(f"Thanks! ~ {sales_person}")

sale()