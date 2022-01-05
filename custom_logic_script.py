# My custom logic Script

def main():
    #!/usr/bin/env python3
    """Alta3 Research | RZFeeser
    if, elif, else - A simple program using conditionals to make a decision."""


    errorMessage = "You need to select a valid option" #Displayed if user input doesnt match choice
    choices = '\n 0. AMZN\n 1. TSLA\n 2. MSFT\n 3. GOOGL'
    data = [
        { "company": "Amazon", "price": 3296.40, "p/e": 64.46 },
        { "company": "Tesla", "price": 1090.90, "p/e": 354.00 },
        { "company": "Microsoft", "price": 317.04, "p/e": 35.44 },
        { "company": "Google", "price": 2755.23, "p/e": 26.54 }]

    
    # wrap connection in a float() to accept decimals as numbers
    choice = float(input("Select stock to analyze" + choices))

    # must match indexes in data. Could be refactored to variable
    # i.e. printCompanyData(data[choice])
    if choice == 0:
        printCompanyData(data[0])
    elif choice == 1:
       printCompanyData(data[1])
    elif choice == 2:
        printCompanyData(data[2])
    elif choice == 3:
        printCompanyData(data[3])
    else:
        print(errorMessage)

#Prints data of selected company in human readable way
def printCompanyData(obj):
    print(f"{obj['company']} - Price: {obj['price']} P/E: {obj['p/e']}")

if __name__ == "__main__":
    main()
