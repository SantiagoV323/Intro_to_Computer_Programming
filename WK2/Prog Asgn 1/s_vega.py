# Hotel signing for customers. Defining cost per day, getting guest name and number of days staying, calculating total cost and printing hotel logo.

cost_per_day = 65.5

#define main function
def main(): 
    #greeting
    print("Welcome to hotel Palermo!")
    #get guest name and number of days staying
    guest = input("Please write your name: ")
    #greeting customer by name, get number of days staying and print cost per day
    days = int(input(f"Hello {guest}, how many days will you be staying with us?,\nthe cost per day is $ {cost_per_day} dollars: "))
    #calculate total cost    
    total = days * cost_per_day
    #print hotel logo
    print("""    @..@
   (----)
  ( >__< )
  ^^ ~~ ^^""")
    #print total cost message
    print(f"Thank you {guest}, your total cost for {days} days is: $ {total} dollars. We hope you enjoy your stay!")
#call main function
main()