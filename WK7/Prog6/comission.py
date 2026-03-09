# Sales Commission Calculator
# Ask for a salesperson's daily sales (Mon–Sun), total them, and calculate a 25% commission.
# Santiago 
# 2026-02-26 

def main():
    # Tell the user the purpose of the program
    print("This program calculates a salesperson's total weekly sales and commission (25%).")

    # Ask for the salesperson's name
    salesperson_name = input("Enter the salesperson's name: ")

    # Days of the week (Mon–Sun)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    total_sales = 0.0  # accumulator for total weekly sales

    # Loop through 7 days and ask for sales each day
    for day in days:
        sales_for_day = float(input(f"Enter sales for {day}: "))
        total_sales = total_sales + sales_for_day

    # Calculate commission (25%)
    commission_rate = 0.25
    commission = total_sales * commission_rate

    print("\n--- Weekly Sales Summary ---")
    print(f"Salesperson: {salesperson_name}")
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Commission (25%): ${commission:.2f}")


main()