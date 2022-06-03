# check budget function (05)

"""I decided that anyone who's using this program is probably smart enough to not
   enter anything they can't afford, so if they do ask for something over budget,
   it will tell them it's not in budget."""


def enter_budget(question):
    while True:
        input_string = input(question)
        if input_string == "":
            print("*** You cannot leave this empty ***")
        else:
            try:
                float(input_string)
            except ValueError:
                print("*** Please input a valid integer ***")
            else:
                if float(input_string) < 0.009:
                    print("*** Please input a number above 0 ***")
                else:
                    return float(input_string)


def enter_price(question):
    while True:
        input_string = input(question)
        if input_string == "":
            print("*** You cannot leave this empty ***")
        else:
            try:
                float(input_string)
            except ValueError:
                print("*** Please input a valid integer ***")
            else:
                if float(input_string) < 0.009:
                    print("*** Please input a number above 0. ***")
                else:
                    return float(input_string)


budget = enter_budget("What is your budget? $")  # asks for budget
price = enter_price("What is the price of the thing? $")  # asks for price
if price > budget:  # checks if the price is more than the budget
    print("over budget")
else:
    print("in budget")  # outputs over or under budget depending on if the user has enough money
