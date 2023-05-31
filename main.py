import bestbuy.products
import bestbuy.store


def display_menu():
    """
    Displays the main menu that shows all the options available to the user.
    @return:
    """
    message = (
            "\nStore Menu" +
            "\n----------" +
            "\n1. List all products in store" +
            "\n2. Show total amount in store" +
            "\n3. Make an order" +
            "\n4. Quit"
    )
    print(message)


def goodbye(purchase=False):
    """
    This method will simply print a different variation of goodbye message based on the
    customer's behaviour.
    @param purchase:
    @return:
    """
    if purchase:
        print("\n\n\t\tThank you for your custom. Please visit again!")
    else:
        print("\n\n\t\tThank you. Goodbye!")


def get_user_option(prompt, valid_options) -> int:
    """
    Validates and returns user's main menu options input.
    @return:
    """
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print("Error with your choice! Try again!")
        else:
            if user_input not in valid_options:
                print(f"Please enter a number between {valid_options[0]} and {valid_options[-1]}")
            else:
                return user_input
        display_menu()


def list_all_products(best_buy) -> str:
    """
    Prints the str of all the active products in the current store
    @return:
    """
    message = "------\n"
    all_products = [product for product in best_buy.get_all_products()]
    i = 1
    for product in all_products:
        message += f"{i}. {product.show()}\n"
        i += 1
    message += "------"
    return message


def get_total_qty(best_buy) -> float:
    """
    Displays the total quantity of all active products combined
    @return:
    """
    all_products = [product for product in best_buy.get_all_products()]
    total_qty = 0
    for product in all_products:
        total_qty += product.get_quantity()
    return total_qty


def update_basket(basket, product, product_quantity) -> object:
    """
    Low-level method to update the basket when a user adds a product to the list of items
    that they want to purchase.
    Caller: place_order()
    @param basket:
    @param product:
    @param product_quantity:
    @return:
    """
    updated_basket = []
    if product not in ([item[0] for item in basket]):
        basket.append((product, product_quantity))
        updated_basket = basket.copy()
    else:
        for product_qty in basket:
            if product == product_qty[0]:
                old_qty = product_qty[1]
                # print(old_qty)  # -> @TEST
                updated_basket.append((product, old_qty + product_quantity))
            else:
                updated_basket.append((product_qty[0], product_qty[1]))
    print("Product added to list!\n")
    # print(updated_basket)  # -> @TEST
    return updated_basket


def has_enough_qty(basket) -> bool:
    """
    Checks if there are enough quantity of products in a store for a user to purchase
    @param basket:
    @return:
    """
    for item in basket:
        product = item[0]
        quantity = item[1]
        available_qty = product.get_quantity()
        if available_qty < quantity:
            return False
    return True


def place_order(best_buy):
    """
    Runs in a loop to allow a user to make a purchase.
    @return:
    """
    product_list = best_buy.get_all_products()
    basket = []
    print(list_all_products(best_buy))
    print("When you want to finish order, enter empty text.")
    while True:
        product_number = input("Which product # do you want?")
        # print(f"Product number: {product_number}")  # -> @TEST
        product_quantity = input("What amount do you want?")
        # print(f"Product quantity: {product_quantity}")  # -> @TEST
        if product_number != "" and product_quantity != "":
            try:
                product_number = int(product_number)
                product_quantity = float(product_quantity)
                product = product_list[product_number - 1]
            except TypeError:
                print("Error adding product!\n")
                continue
            except IndexError:
                print("Error adding product!\n")
                continue
            else:
                basket = update_basket(basket, product, product_quantity)
        else:  # CHECKOUT
            if basket:
                # print(basket)  # -> @TEST
                if has_enough_qty(basket):
                    total_price = 0
                    total_price += best_buy.order(basket)
                    print("********")
                    print(f"Order made! Total payment: {total_price}")
                    return
                else:
                    # Not enough quantity of at least one product in store.
                    # No purchase made. Display error message and return to main menu!
                    print("Error while making order! Quantity larger than what exists")
                    return
            else:  # Basket is empty. Return to main menu!
                return


def start(best_buy, valid_options):
    """
    This is the program in the console.
    @return:
    """
    finished = False
    while not finished:
        display_menu()
        option = get_user_option("Please choose a number: ", valid_options)
        if option == 1:  # 1. List all products in store
            print(list_all_products(best_buy))
        elif option == 2:  # 2. Show total amount in store
            print(f"Total of {get_total_qty(best_buy)} item in store")
        elif option == 3:  # 3. Make an order
            place_order(best_buy)
        elif option == 4:  # 4. Quit
            goodbye(purchase=False)
            finished = True
        else:  # Something unknown went wrong here. Continue...
            continue


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    valid_options = [1, 2, 3, 4]
    try:
        start(best_buy, valid_options)
    except KeyboardInterrupt:
        goodbye()


if __name__ == "__main__":
    main()
