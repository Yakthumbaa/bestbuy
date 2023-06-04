import main
import pytest
import products
# import promotions


def test_has_enough_qty():
    # Instantiate some products for TEST
    macbook_air_m2 = products.Product("MacBook Air M2", price=1450, quantity=100)
    windows_license = products.NonStockedProduct("Windows License", price=125)
    google_pixel = products.Product("Google Pixel 7", price=500, quantity=250)

    basket = ((macbook_air_m2, 101), (windows_license, 1), (google_pixel, 10))
    assert main.has_enough_qty(basket) is False
    basket = ((macbook_air_m2, 100), (windows_license, 1000), (google_pixel, 10))
    assert main.has_enough_qty(basket) is True


def test_update_basket():
    # Instantiate some products for TEST
    macbook_air_m2 = products.Product("MacBook Air M2", price=1450, quantity=100)
    windows_license = products.NonStockedProduct("Windows License", price=125)
    google_pixel = products.Product("Google Pixel 7", price=500, quantity=250)

    basket = [(macbook_air_m2, 10), (windows_license, 1), (google_pixel, 10)]
    updated_basket = [(macbook_air_m2, 15), (windows_license, 1), (google_pixel, 10)]
    assert main.update_basket(macbook_air_m2, 5, basket) == updated_basket
    basket = [(macbook_air_m2, 10), (windows_license, 1), (google_pixel, 10)]
    updated_basket = [(macbook_air_m2, 10), (windows_license, 22), (google_pixel, 10)]
    assert main.update_basket(windows_license, 21, basket) == updated_basket


pytest.main()
