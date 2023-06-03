from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Promotion is an abstract class from which all other promotions will be derived.
    """

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
            This method gets 2 parameters - a product instance and a quantity, and returns the discounted price
            after promotion was applied.
            --> To be implemented by the child class.
            :param product:
            :param quantity:
            :return:
            """
        pass


class PercentageDiscount(Promotion):
    """
    This is a promotion for 20% off the price of an item.
    """

    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity) -> float:
        """
        Returns the price after the discount is applied
        :param product:
        :param quantity:
        :return:
        """
        return (product.price * 0.8) * quantity


class SecondHalfOff(Promotion):
    """
    This is a promotion for 50% off the second item.
    """

    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity) -> float:
        """
        Returns the price after the discount is applied
        :param product:
        :param quantity:
        :return:
        """
        valid_qty = quantity // 2  # The promotion only applies to every other item
        """
        remaining_qty = quantity - valid_qty
        discounted_price = product.price * 0.5
        total_price = (valid_qty * discounted_price) + (product.price * remaining_qty)
        """
        return (product.price * 0.5 * valid_qty) + (product.price * (quantity - valid_qty))


class Buy2Get1Free(Promotion):
    """
    This is a promotion for 100% off the price of the 3rd item.
    """

    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity) -> float:
        """
        Returns the price after the discount is applied
        :param product:
        :param quantity:
        :return:
        """
        valid_qty = quantity // 3  # The promotion only applies to every third item
        return product.price * (quantity - valid_qty)
