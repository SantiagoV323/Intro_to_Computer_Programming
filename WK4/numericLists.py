# Example of creating a list, and use of min, max, sum, and len functions with numeric lists
def main ():
    scores = [85, 79, 99, 100]
    print("Scores:", scores)
    total = sum(scores) # Sum function works with numeric lists
    print("Total score:", total)
    avg = total / len(scores) # len function gives the number of elements in the list
    print("Average score:", avg)
    highest = max(scores) # max function finds the highest value in the list
    print("Highest score:", highest)
    lowest = min(scores) # min function finds the lowest value in the list
    print("Lowest score:", lowest)

main()