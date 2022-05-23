def input_checker(question):
    output = ""
    running = True
    while running:
        input_string = input(question)
        if input_string == "":
            print("You cannot leave this empty\n")
        else:
            try:
                float(input_string)
            except ValueError:
                print("Please input a valid integer\n")
            else:
                if float(input_string) < 0:
                    print("Please input a number above 0\n")
                else:
                    output = float(input_string)
                    running = False
    print(f"Budget = ${output:.2f}")


input_checker("Please enter your budget: ")
