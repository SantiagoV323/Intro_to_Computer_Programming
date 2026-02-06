# Andres Santiago Vega Franco T-20331228
# 02/05/2026

# This program calculates the total earnings for an employee based on hours worked.
# It prompts for the employee's name, hourly wage, and Saturday hours, then computes
# the total hours worked (excluding zero-hour days) and displays the payment summary.

def main ():
    hours = [6.75, 8.25, 10.75, 0.0, 8.25]
    print ('')
    first_name = input ('Enter the first name of the employee: ')
    last_name = input ('Enter the last name of the employee: ')

    # Asking the user for the hourly wage, featuring the employee's name for a more personalized experience.
    hourly_wage = float (input (f"Enter the hourly wage for {first_name} {last_name}: "))

    saturdays = float(input ('Enter the number of hours worked on Saturdays: '))
    # Adding the hours worked on Saturdays to the list hours.
    hours.append (float (saturdays))
    # Calculating the total of hours worked by summing the elements in the list hours.
    total_hours = sum (hours)
    # Calculating the total earnings by multiplying the total hours worked by the hourly wage
    total_earnings = total_hours * hourly_wage
    # remove the (single) zero hours day
    hours.remove (0.0)
    # Number of days worked
    days_worked = len (hours)

    print (f'{first_name} {last_name} has worked: {days_worked} days, a total of {total_hours:.2f} hours, with a wage of {hourly_wage:.2f} per hour, for a total of $ {total_earnings:.2f}')

main ()
