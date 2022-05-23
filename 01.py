def integer_checker(question):
    valueerror = "Sorry, you must enter an integer\n"
    blankerror = "You can't leave this blank\n"
    negerror = "Please enter a number greater than 0\n"
    number = ""
    while not number:
        input_string = input(question)
        if input_string == "":
            print(blankerror)
        elif input_string.isnumeric() and float(input_string) < 0:
            print(negerror)
        else:
            try:
                number = float(input_string)
            except ValueError:
                print(valueerror)
    return number


budget = integer_checker("Please enter your budget: ")
print(f"Budget = ${budget:.2f}")
