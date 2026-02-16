# Andres Santiago Vega Franco
# T-20331228
# 02/15/2026
# Shipping cost calculator
# This program calculates shipping cost based on total purchase amount.

def main():
    print("Shipping Cost Calculator")

    purchase = float(input("Enter total purchase amount: $"))

    if purchase >= 600:
        shipping = 0.00
    elif purchase >= 300:
        shipping = 5.00
    elif purchase >= 100:
        shipping = 8.00
    else:
        shipping = 15.00

    total = purchase + shipping

    print(f"\nPurchase amount: ${purchase:.2f}")
    print(f"Shipping cost: ${shipping:.2f}")
    print(f"Total cost: ${total:.2f}")

main()
