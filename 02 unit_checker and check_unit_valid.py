def unit_checker(question):
    valid_units = ["kg", "KG", "Kg", "kG", "L", "l", "G", "g", "mg", "MG", "Mg", "mG", "ml", "ML", "Ml", "mL"]
    running = True
    while running:
        input_string = input(question)
        if input_string == "":
            print("You cannot leave this blank.")
        else:
            if input_string not in valid_units:
                print("Please input a valid unit (kg, ml, L, etc.)")
            else:
                output1 = input_string
                running = False
    print(f"you have selected: {output1}")


unit_checker("Which unit are you using?: ")

