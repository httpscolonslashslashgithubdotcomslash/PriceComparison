def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


budget = integer_checker("Please enter your budget: ")
while budget <0:
    print("Please enter a number greater than 0: ")
    budget = integer_checker("Please enter your budget: ")
print(f"Budget = {budget}")
