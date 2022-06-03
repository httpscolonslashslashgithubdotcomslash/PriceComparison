# main program
# Connor Chase

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


def best_value(product_list):
    if not product_list:
        pass
    else:
        min_list = []
        for product in product_list:
            min_list.append(
                product[3])  # this appends the PPU from product_list so it can search for the least expensive.
        minitem = min(min_list)
        minindex = min_list.index(minitem)
        print(f"The best value item is {product_list[minindex][0]} with a PPU of {minitem:.2f}")
        return minindex


def worst_value(product_list):
    if not product_list:
        pass
    else:
        max_list = []
        for product in product_list:
            max_list.append(product[3])
        maxitem = max(max_list)
        maxindex = max_list.index(maxitem)
        print(f"The worst value item is {product_list[maxindex][0]} with a PPU of {maxitem:.2f}")
        return maxindex


product_list = []
budget = enter_budget("Please enter your budget: $")
running = True

while running:
    loop = True
    yesno = input("\nDo you want to add another item (yes or y)? ")
    if yesno == "yes" or yesno == "y":
        while loop:
            name = product_name("\nWhat is the product you want? ")
            weight = price_per_unit(f"\nWhat is the net weight of one {name} (in grams)?: ")
            price = enter_price(f"\nWhat is the price of one {name}? $")
            if price > budget:
                print("\nYou cannot afford this item.")
                break
            else:
                ppu = float(price * (100 / weight))
                print(f"\nYou want a {name}, costing ${price:.2f} with a price per 100g of ${ppu:.2f}.")
                product_list.append([name, weight, price, ppu])
                loop = False
    else:
        exit = input("Are you sure you want to exit this program? ")
        if exit == "y" or exit == "yes":
            print("Thank you for using this program.")
            running = False
        else:
            continue

for product in sorted(product_list, key=lambda prod: prod[3]):
    print(f"Item: {product[0]}. Weight: {product[1]}g. "
          f"Price: ${product[2]:.2f}. PPU: ${product[3]:.2f}.")
best_value(product_list)
worst_value(product_list)
