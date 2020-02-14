import pytest
from pages.product_page import ProductPage

list_links = [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}' for i in range(10) if i != 7]
list_links.insert(7, pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail))

@pytest.mark.parametrize('link', list_links)
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
