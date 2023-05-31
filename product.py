class Product:

    def __init__(self, name, price, quantity):
        """
        Constructor --> If an argument is blank then this method throws ValueError Exception.
        This exception needs to be handled by the caller.
        :raises ValueError: if an argument is an empty string.
        @param name:
        @param price:
        @param quantity:
        """
        if not name or not price or not quantity:
            raise ValueError("Required parameter: Argument cannot be blank!")
        elif price < 0 or quantity < 0:
            raise ValueError("Price and/or quantity cannot be a negative number!")
        else:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
            # self.active = True if quantity > 0 else False

    def get_quantity(self) -> float:
        """
        Getter method to return the quantity of the product available in stock
        @return:
        """
        return self.quantity

    def set_quantity(self, new_quantity):
        """
        Setter method to change the quantity in stock to the new quantity. Every time the quantity is
        changed, is_active() will be toggled depending on the condition.
        @param new_quantity:
        @return:
        """
        self.quantity = new_quantity
        if self.quantity == 0:
            self.deactivate()
        else:  # if we decide to add a feature to re-stock in the future
            self.activate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Method to make a purchase. The product quantity updates once a purchase is made. The total
        price is returned by this method and raises ValueError if a buyer tries to purchase more
        than the quantity in stock.
        :raises ValueError: if available quantity less than quantity the buyer wants to purchase.
        @param quantity:
        @return:
        """
        if quantity > self.quantity:
            raise ValueError(f"There is not enough in stock. Available quantity = {self.quantity}")
        else:
            self.set_quantity(self.quantity - quantity)
            total_price = self.price * quantity
        return total_price

    """
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def sell(self, amount):
        self.quantity -= amount

    """
