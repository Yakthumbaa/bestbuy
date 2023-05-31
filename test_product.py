import pytest
import product


def test_create_product_good():
    """
    Testing the constructor with good arguments.
    """
    macbook_air_m2 = product.Product("MacBook Air M2", price=1450, quantity=100)
    assert macbook_air_m2.name == "MacBook Air M2"
    assert macbook_air_m2.price == 1450
    assert macbook_air_m2.quantity == 100
    assert macbook_air_m2.is_active() is True


def test_create_product_bad():
    """
    Test that creating a product with invalid details (empty name, negative price) invokes an exception.
    """
    with pytest.raises(ValueError, match="Required parameter: Argument cannot be blank!"):
        product.Product("", price=500, quantity=250)
        product.Product("", price=0, quantity=250)
        product.Product("Nothing Phone (1)", price=500, quantity=0)
    with pytest.raises(ValueError, match="Price and/or quantity cannot be a negative number!"):
        product.Product("Google Pixel 7", price=-1, quantity=-10)
        product.Product("Google Pixel 7", price=-1, quantity=10)
        product.Product("Google Pixel 7", price=500, quantity=-10)


def test_inactive_when_zero():
    """
    Test that when a product reaches 0 quantity, it becomes inactive.
    """
    macbook_air_m2 = product.Product("MacBook Air M2", price=1450, quantity=100)
    macbook_air_m2.buy(100)
    assert macbook_air_m2.is_active() is False
    macbook_air_m2.set_quantity(2)
    assert macbook_air_m2.is_active() is True


def test_buy_modifies_qty():
    """
    Test that product purchase modifies the quantity and returns the right output.
    """
    macbook_air_m2 = product.Product("MacBook Air M2", price=1450, quantity=100)
    macbook_air_m2.buy(22)
    assert macbook_air_m2.quantity == 78
    macbook_air_m2.buy(58)
    assert macbook_air_m2.quantity == 20


def test_buy_too_much():
    """
    Test that buying a larger quantity than exists invokes exception.
    """
    macbook_air_m2 = product.Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError, match=f"There is not enough in stock. "
                                         f"Available quantity = {macbook_air_m2.quantity}"):
        macbook_air_m2.buy(101)


pytest.main()
