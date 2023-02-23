# ======== Shoe class ==========
class Shoe:
    # Defining class constructor
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Creating get_cost method
    def get_cost(self):
        return self.cost

    # Creating get_quantity method
    def get_quantity(self):
        return self.quantity

    # Creating user-friendly output
    def __str__(self):
        output = f"\nCountry: {self.country}\n"
        output += f"Code: {self.code}\n"
        output += f"Product: {self.product}\n"
        output += f"Cost: {self.cost}\n"
        output += f"Quantity: {self.quantity}\n"
        return output

# ============= Shoe list ===========
# The shoe list will be used to store a list of objects of shoes.
shoe_list = []


# ========== Functions outside the Shoe class ==============
# Creating read_shoes_data function
def read_shoes_data():
    try:
        f = open("inventory.txt", "r")
        inventory = f.readlines()

        for shoe_object in inventory:
            # Skipping the first line of the inventory.txt file
            if shoe_object.startswith("Country"):
                pass

            # Appending each line (i.e. shoe_object) to the shoe_list
            else:
                content = shoe_object.strip().split(",")
                country = content[0]
                code = content[1]
                product = content[2]
                cost = content[3]
                quantity = content[4]
                shoes = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoes)

        f.close()

    # Preventing the programme to crash in case the file cannot be found
    except FileNotFoundError:
        print("Error, an inventory file has not been supplied")


# Creating capture_shoes function, allowing user to input new shoes and adding it to shoe_list
def capture_shoes():
    shoe_country = input("Enter country: ")
    shoe_code = input("Enter code: ").upper()
    shoe_product = input("Enter product: ").capitalize()
    shoe_cost = input("Enter cost: ")
    shoe_quantity = input("Enter quantity: ")
    new_shoes = Shoe(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity)
    shoe_list.append(new_shoes)
    print("The shoes have been successfully added!\n")


# Creating view_all function, and display all data in a user-friendly way
def view_all():
    for shoe in shoe_list:
        print(shoe)


# Creating re_stock function
def re_stock():
    # Finding the pair of shoes with the lowest quantity in stock
    lowest_quantity = min(shoe_list, key=lambda shoe: int(shoe.quantity))
    index = shoe_list.index(lowest_quantity)
    print(f"There are only {lowest_quantity.quantity} pairs of {lowest_quantity.product} "
          f"in stock in {lowest_quantity.country}.")

    # Asking user if they want to restock
    restock = input("Would you like to restock this product? (Enter Y or N): ").upper()

    # If user agrees, update data in shoe_list
    if restock == "Y":
        while True:
            try:
                quantity = int(input("Enter the new quantity wanted for this product: "))

                shoe_object = Shoe(lowest_quantity.country, lowest_quantity.code,
                                   lowest_quantity.product, lowest_quantity.cost, quantity)
                shoe_list[index] = shoe_object
                print("The quantity has been updated for this product!\n")

                # Update data in txt file as well
                f = open("inventory.txt", "w+")
                lowest_quantity.quantity = quantity

                for shoe in shoe_list:
                    f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

                f.close()
                break

            # Preventing the programme from crashing in case user doesn't insert a number
            except ValueError:
                print("Invalid input. Please enter a number: ")

    # Display message if user doesn't want to restock the product
    elif restock == "N":
        print("No worries!")

    # Display error message if the user has inserted something else than the options above
    else:
        print("Incorrect input, please try again")


# Creating search_shoe function to allow user to retrieve data from a product by inserting its code
def search_shoe():
    user_code = input("Enter the product code: ")

    for item in shoe_list:
        if user_code == item.code:
            print(item)


# Creating value_per_item function to calculate the total value for each product in stock
def value_per_item():
    for item in shoe_list:
        print(f"\n{item.product}:")
        print(f"£{float(item.cost) * float(item.quantity)}")


# Creating highest_qty function to display "for sale" message for item that has the highest quantity in stock
def highest_qty():
    largest_quantity = max(shoe_list, key=lambda shoe: int(shoe.quantity))
    print(f"{largest_quantity.product} are for sale!")


# Calling read_shoes_data function so the system reads the data from the txt file
read_shoes_data()

# ========== Main Menu =============
menu = "========== Main Menu =============\n"
menu += "ca - To enter a new pair of shoes\n"
menu += "va - To view all shoes in stock\n"
menu += "st - To restock the pair of shoes that has the smallest quantity in stock\n"
menu += "se - To search for a specific shoe\n"
menu += "tot - To calculate the total value for each item\n"
menu += "hi - Print the shoe with the highest quantity as for sale\n"
menu += "e - Exit the menu\n"
print(menu)

# If statements calling the functions depending on the user's choice
while True:
    choice = input("What would you like to do? ").lower()

    if choice == "ca":
        capture_shoes()

    elif choice == "va":
        view_all()

    elif choice == "st":
        re_stock()

    elif choice == "se":
        search_shoe()

    elif choice == "tot":
        value_per_item()

    elif choice == "hi":
        highest_qty()

    elif choice == "e":
        print("Goodbye!!!")
        break

    else:
        print("Please select your option from the menu above!")
