"""
Product class is the parent class which is extended by two classes:
a) NonStockedProduct - non-physical products such as (digital license) Microsoft Windows license
                         should always have their quantity set to 0 but active.
b) LimitedProduct - this can only be purchased once e.g. delivery charge, etc.
"""


class Product:

    def __init__(self, name, price, quantity, promotion=None):
        """
        Constructor --> If an argument is blank then this method throws ValueError Exception.
        This exception needs to be handled by the caller.
        :raises ValueError: if an argument is an empty string.
        :param name:
        :param price:
        :param quantity:
        """
        if not name or not price or (not quantity and quantity < 0):
            raise ValueError("Required parameter: Argument cannot be blank!")
        elif price < 0 or quantity < 0:
            raise ValueError("Price and/or quantity cannot be a negative number!")
        else:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.promotion = promotion
            self.active = True
            # self.active = True if quantity > 0 else False

    def get_promotion(self) -> object:
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, new_quantity):
        """
        Setter method to change the quantity in stock to the new quantity. Every time the quantity is
        changed, is_active() will be toggled depending on the condition.
        :param new_quantity:
        :return: None
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

    def buy(self, quantity) -> float:
        """
        Method to make a purchase. The product quantity updates once a purchase is made. The total
        price is returned by this method and raises ValueError if a buyer tries to purchase more
        than the quantity in stock.
        :raises ValueError: if available quantity less than quantity the buyer wants to purchase.
        :param quantity:
        :return:
        """
        if quantity > self.quantity:
            raise ValueError(f"There is not enough in stock. Available quantity = {self.quantity}")
        else:
            self.set_quantity(self.quantity - quantity)
            if self.promotion:
                total_price = self.promotion.apply_promotion(self, quantity)
            else:
                total_price = self.price * quantity
        return total_price

    def show(self) -> str:
        if self.promotion:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, " \
                   f"Promotion: {self.promotion.name}"
        else:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


class NonStockedProduct(Product):
    """
    Some products in the store are not physical, so we don’t need to keep track of their quantity.
    For example - a Microsoft Windows license. On these products, the quantity should be set to
    zero and always stay that way.
    """

    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def set_quantity(self, new_quantity):
        """
        This method will raise an error since this type of product will always have their
        quantity set to zero.
        A) We could either raise error
        :raises ValueError: if this method is called by an instance of this class
        --> raise AttributeError("'NonStockedProduct' has no attribute 'set_quantity'")
        B) Or simply set the quantity to zero
        """
        # Chose option B
        self.quantity = 0

    def buy(self, quantity) -> float:
        """
        :Override: This class should allow unlimited purchases even when the quantity is always 0
        :param quantity:
        :return:
        """
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity
        return total_price

    def show(self) -> str:
        if self.promotion:
            return f"{self.name}, Price: {self.price}, Promotion: {self.promotion.name}"
        else:
            return f"{self.name}, Price: {self.price}"


class LimitedProduct(Product):
    """
    Some products can only be purchased X times in an order. For example - a shipping fee can only be added once.
    If an order is attempted with quantity larger than the maximum one, it should be refused with an exception.
    """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, purchase_qty) -> float:
        """
        Method to make a purchase. The product quantity updates once a purchase is made. The total
        price is returned by this method and raises ValueError if a buyer tries to purchase more
        than the quantity in stock.
        :raises ValueError: if available quantity less than quantity the buyer wants to purchase
        OR, if a buyer wants to purchase more than the maximum allowed per customer.
        :param purchase_qty:
        :return:
        """
        if self.quantity < purchase_qty <= self.maximum:
            raise ValueError(f"There is not enough in stock. Available quantity = {self.quantity}")
        elif purchase_qty > self.maximum:
            raise ValueError(f"A maximum of {self.maximum} units allowed per customer.")
        else:
            self.set_quantity(self.quantity - purchase_qty)
            if self.promotion:
                total_price = self.promotion.apply_promotion(self, purchase_qty)
            else:
                total_price = self.price * purchase_qty
        return total_price

    def show(self) -> str:
        if self.promotion:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, " \
                   f"Maximum: {self.maximum}, Promotion: {self.promotion.name}"
        else:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, " \
                   f"Maximum: {self.maximum}"


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