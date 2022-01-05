# Lab 24 ipv4 testing

def main():
    #!/usr/bin/env python3
    """Alta3 Research | RZFeeser
    if, elif, else - A simple program using conditionals to make a decision."""


    message = 'Your grade: '

    # wrap connection in a float() to accept decimals as numbers
    score = float(input("What was your score on the test?"))

    # if input value was higher or equal to 25
    if score >= 90:
        message = message + 'A'
    elif score >= 80:
        message = message + 'B'
    elif score >= 70:
        message = message + 'C'
    else:
        message = "You Failed..."
    print(message)


if __name__ == "__main__":
    main()
