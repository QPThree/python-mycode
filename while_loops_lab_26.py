# Lab 26

#!/usr/bin/env python3

def main():
    round = 0
    answer = ' '
    while round < 3 and answer.lower() != "brian":
        round += 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your answer --> ")
        if answer.lower() == "brian":
            print("Correct")
            break
        elif answer.lower() == "shrubbery":
            print("You got the secret answer!")
            break
        elif round == 3:
            print("Sorry, the answer was Brian.")
            break
        else:
            print("Sorry! Try again!")

if __name__ == "__main__":
    main()