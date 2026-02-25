# testing whether a for loop can step through a string

def main():
    course = 'Intro to Programming'
    # print backwards
    for letter in reversed(course):
        print(f'{letter}', end=' ')

main()