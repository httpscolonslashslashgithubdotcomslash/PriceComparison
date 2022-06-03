def product_name(question):
    while True:
        input_string = str(input(question))
        if not input_string:
            print("*** You cannot leave this blank. ***")
            continue
        elif input_string[0].isnumeric():
            print("*** Can't be numeric ***")
        elif input_string[0].isspace():
            print("*** You cannot leave thus blank. ***")
        else:
            return input_string


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


def price_per_unit(question):
    while True:
        input_string = input(question)
        if input_string == "":
            print("*** You cannot leave this empty ***")
        else:
            try:
                int(input_string)
            except ValueError:
                print("*** Please input a valid integer ***")
            else:
                if int(input_string) < 1:
                    print("Please input a number above 0")
                else:
                    return int(input_string)


product_list = []
running = True
number = 0

while running:
    loop = True
    yesno = input("\nDo you want to add another item (yes or y)? ")
    if yesno == "yes" or yesno == "y":
        while loop:
            name = product_name("\nWhat is the product you want? ")
            weight = price_per_unit(f"\nWhat is the net weight of one {name} (in grams)?: ")
            price = enter_price(f"\nWhat is the price of one {name}? $")
            ppu = float(price * (100 / weight))
            print("\nFinished")
            product_list.append([name, weight, price, ppu])
            loop = False
    else:
        running = False

for i in product_list:
            print(f"Item: {product_list[number][0]}. Weight: {product_list[number][1]}g. "
                  f"Price: ${product_list[number][2]:.2f}. PPU: ${product_list[number][3]:.2f}.")
            number += 1
