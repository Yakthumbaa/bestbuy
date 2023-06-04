import pytest
import products
import promotions


def test_create_product_good():
    """
    Testing the constructor with good arguments.
    """
    macbook_air_m2 = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert macbook_air_m2.name == "MacBook Air M2"
    assert macbook_air_m2.price == 1450
    assert macbook_air_m2.quantity == 100
    assert macbook_air_m2.is_active() is True


def test_create_product_bad():
    """
    Test that creating a product with invalid details (empty name, negative price) invokes an exception.
    """
    with pytest.raises(ValueError, match="Required parameter: Argument cannot be blank!"):
        products.Product("", price=500, quantity=250)
        products.Product("", price=0, quantity=250)
        products.Product("Nothing Phone (1)", price=500, quantity=0)
    with pytest.raises(ValueError, match="Price and/or quantity cannot be a negative number!"):
        products.Product("Google Pixel 7", price=-1, quantity=-10)
        products.Product("Google Pixel 7", price=-1, quantity=10)
        products.Product("Google Pixel 7", price=500, quantity=-10)


def test_inactive_when_zero():
    """
    Test that when a product reaches 0 quantity, it becomes inactive.
    """
    macbook_air_m2 = products.Product("MacBook Air M2", price=1450, quantity=100)
    macbook_air_m2.buy(100)
    assert macbook_air_m2.is_active() is False
    macbook_air_m2.set_quantity(2)
    assert macbook_air_m2.is_active() is True


def test_buy_modifies_qty():
    """
    Test that product purchase modifies the quantity and returns the right output.
    """
    macbook_air_m2 = products.Product("MacBook Air M2", price=1450, quantity=100)
    macbook_air_m2.buy(22)
    assert macbook_air_m2.quantity == 78
    macbook_air_m2.buy(58)
    assert macbook_air_m2.quantity == 20


def test_buy_too_much():
    """
    Test that buying a larger quantity than exists invokes exception.
    """
    macbook_air_m2 = products.Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError, match=f"There is not enough in stock. "
                                         f"Available quantity = {macbook_air_m2.quantity}"):
        macbook_air_m2.buy(101)


def test_virtual_goods():
    """
    Testing for child class NonStockedProduct. Virtual products have quantity = 0 but a customer
    should be able to buy them nonetheless.
    """
    # Instantiate a NonStockedProduct
    windows_license = products.NonStockedProduct("Windows License", price=125)
    assert windows_license.quantity == 0
    windows_license.set_quantity(20)
    assert windows_license.quantity == 0
    # Test buy
    assert windows_license.buy(1) == 125
    assert windows_license.buy(3) == 375
    assert windows_license.buy(10) == 1250
    # Test the show method
    assert windows_license.show() == f"{windows_license.name}, Price: {windows_license.price}"


def test_limited_goods():
    """
    Testing for child class LimitedProduct
    """
    # Instantiate a LimitedProduct
    shipping_fee = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    # Test 1 legal purchase
    assert shipping_fee.buy(1) == 10
    # Test case where a purchase quantity is greater than maximum
    with pytest.raises(ValueError, match=f"A maximum of {shipping_fee.maximum} units "
                                         f"allowed per customer."):
        shipping_fee.buy(2)
    # The total quantity should be...
    assert shipping_fee.quantity == 249
    # Test scenario where the total quantity of product is fully purchased
    for i in range(shipping_fee.quantity):
        shipping_fee.buy(1)
    assert shipping_fee.quantity == 0
    # Test out of stock...
    with pytest.raises(ValueError, match=f"There is not enough in stock. "
                                         f"Available quantity = {shipping_fee.quantity}"):
        shipping_fee.buy(1)
    # Finally, test the show method
    assert shipping_fee.show() == f"{shipping_fee.name}, Price: {shipping_fee.price}, " \
                                  f"Quantity: {shipping_fee.quantity}, Maximum: {shipping_fee.maximum}"


def test_product_with_promotion():
    """
    Testing for products with promotions
    """
    # Instantiate some products for TEST
    macbook_air_m2 = products.Product("MacBook Air M2", price=1450, quantity=100)
    windows_license = products.NonStockedProduct("Windows License", price=125)
    google_pixel = products.Product("Google Pixel 7", price=500, quantity=250)

    # Instantiate promotions
    twenty_off = promotions.PercentDiscount("20% off", 20)
    second_half_price = promotions.SecondHalfPrice("Buy 1 get 1 half price")
    buy_2_get_1_free = promotions.ThirdOneFree("Buy 2 get 1 free")

    # Apply promotions 20 % off to macbook and test some cases
    macbook_air_m2.set_promotion(twenty_off)
    assert macbook_air_m2.get_promotion() == twenty_off
    assert macbook_air_m2.buy(1) == 1160

    # Apply promotion second item half price on windows and test some cases
    windows_license.set_promotion(second_half_price)
    assert windows_license.get_promotion() == second_half_price
    assert windows_license.buy(2) == 187.5
    assert windows_license.buy(3) == 312.5

    # Apply promotion buy 2, get 1 free on Google Pixel and test some cases
    google_pixel.set_promotion(buy_2_get_1_free)
    assert google_pixel.get_promotion() == buy_2_get_1_free
    assert google_pixel.buy(5) == 2000


pytest.main()
