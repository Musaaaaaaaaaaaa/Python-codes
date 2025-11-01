###Name: Moosa Shehzad Abbasi
###UID: U37033529
###Brief Description of the program: Retail items(Write a class called RetailItem that has the following data..............)


class RetailItem:
    def __init__(self, item_type, inventory_amount, item_price):
        self.__item_type = item_type
        self.__inventory_amount = inventory_amount
        self.__item_price = item_price

    def __str__(self):
        return f'{self.__item_type.ljust(15)} {str(self.__inventory_amount).rjust(10)} {str(self.__item_price).rjust(10)}'


def main():
    # Prompt the user for the number of items
    num_items = int(input("How many items will you add today? "))

    
    if num_items < 1:
        print("Please enter at least 1 item.")
        return

    items = []  

    # Input item information from the user
    for i in range(num_items):
        item_type = input(f"Name of item {i + 1}: ")
        inventory_amount = int(input(f"Amount of {item_type}: "))
        item_price = float(input(f"Price of {item_type}: "))

        item = RetailItem(item_type, inventory_amount, item_price)
        items.append(item)

    # Display the information in a neat table
    print("Here is a summary of the items you added:")
    print("\nName of Item         Amount   Price($)")
    print("=" * 36)
    for item in items:
        print(item)

if __name__ == "__main__":
    main()
