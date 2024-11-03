class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        """
        Initialize an item with a name, price, and quantity.
        Default values are provided if no input is given.
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        """
        Print the total cost for the item based on its price and quantity.
        """
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")


def main():
    # Let's get the details for the first item
    print("Item 1")
    item1_name = input("What is the name of the item? ")
    item1_price = float(input("How much does it cost? "))
    item1_quantity = int(input("How many are you buying? "))

    # Create the first item
    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

    # Now let's get the details for the second item
    print("\nItem 2")
    item2_name = input("What is the name of the item? ")
    item2_price = float(input("How much does it cost? "))
    item2_quantity = int(input("How many are you buying? "))

    # Create the second item
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    # Print out the cost details for each item
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    # Calculate and show the total cost for both items
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
