import pytest
import promotions
import products

# Note: All validations must be done prior.
# The Promotions classes are basic and will assume that only good arguments are passed.


def test_percentage_discount():
    # Instantiate some products for TEST
    macbook_air_m2 = products.Product("MacBook Air M2", price=1450, quantity=100)
    windows_license = products.NonStockedProduct("Windows License", price=125)
    shipping_fee = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    # Instantiate the promotion
    twenty_off = promotions.PercentageDiscount("20% off")

    # Run Test cases...
    assert twenty_off.name == "20% off"
    assert twenty_off.apply_promotion(macbook_air_m2, 1) == 1160
    assert twenty_off.apply_promotion(windows_license, 10) == 1000
    assert twenty_off.apply_promotion(shipping_fee, 10) == 80


def test_second_half_price():
    # Instantiate some products for TEST
    macbook_air_m2 = products.Product("MacBook Air M2", price=1450, quantity=100)
    windows_license = products.NonStockedProduct("Windows License", price=125)
    shipping_fee = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    # Instantiate the promotion
    second_half_price = promotions.SecondHalfOff("Buy 1 get 1 half price")

    # Run Test cases...
    assert second_half_price.name == "Buy 1 get 1 half price"
    assert second_half_price.apply_promotion(macbook_air_m2, 2) == 2175
    assert second_half_price.apply_promotion(windows_license, 3) == 312.5
    assert second_half_price.apply_promotion(shipping_fee, 5) == 40


def test_buy_2_get_1_free():
    # Instantiate some products for TEST
    macbook_air_m2 = products.Product("MacBook Air M2", price=1450, quantity=100)
    windows_license = products.NonStockedProduct("Windows License", price=125)
    shipping_fee = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    # Instantiate the promotion
    buy_2_get_1_free = promotions.Buy2Get1Free("Buy 2 get 1 free")

    # Run Test cases...
    assert buy_2_get_1_free.name == "Buy 2 get 1 free"
    assert buy_2_get_1_free.apply_promotion(macbook_air_m2, 5) == 5800
    assert buy_2_get_1_free.apply_promotion(macbook_air_m2, 4) == 4350
    assert buy_2_get_1_free.apply_promotion(windows_license, 3) == 250
    assert buy_2_get_1_free.apply_promotion(shipping_fee, 6) == 40


pytest.main()
