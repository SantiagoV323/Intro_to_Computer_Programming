# Andres Santiago Vega Franco
# This program calculates the number of 4-inch servings in a giant sub
# and the cost per serving for each sub entered by the user.

def servings(length_inches):
    return length_inches // 4


def serving_cost(sub_cost, number_of_servings):
    return sub_cost / number_of_servings


def main():

    length_inches = int(input("Enter sub length in inches (-1 to quit): "))

    while length_inches != -1:

        sub_cost = float(input("Enter sub cost: $"))

        number_of_servings = servings(length_inches)

        if number_of_servings > 0:
            cost_per_serving = serving_cost(sub_cost, number_of_servings)

            print("Servings:", number_of_servings)
            print("Cost per serving: $" + format(cost_per_serving, ".2f"))
        else:
            print("Sub is too short to have a serving.")

        length_inches = int(input("Enter sub length in inches (-1 to quit): "))


main()