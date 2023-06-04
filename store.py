class Store:

    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        """
        Method to add a product to the list of available products
        :param product:
        :return:
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        This method is used to remove a product from the list. If the product passed as the argument is not
        on the list, then a ValueError exception is raised - this need to be handled by the caller.
        :raises ValueError: if product to remove does not exist to begin with.
        :param product:
        :return:
        """
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("A non-existent product cannot be removed!")

    def get_total_quantity(self) -> int:
        """
        Returns how many items are in the store in total.
        :return:
        """
        return len(self.products)

    def get_all_products(self) -> list:
        """
        Returns all products in the store that are active.
        :return:
        """
        active_products = [product for product in self.products if product.is_active()]
        return active_products

    @staticmethod
    def order(shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        Note: The ValueError exception is intentionally overlooked since we want the caller to handle
        this exception.
        :raises ValueError: if available quantity less than quantity the buyer wants to purchase.
        :param shopping_list:
        :return:
        """
        total_price = 0
        for item in shopping_list:
            product = item[0]
            quantity = item[1]
            try:
                total_price += product.buy(quantity)
            except ValueError:
                # Catch the Exception but pass it on to the caller
                raise
        return total_price
