from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.click_on_add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_product_in_basket()
        self.should_be_basket_total_equal_price_product()

    def click_on_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_product_in_basket(self):
        product_name1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME1)
        product_name2 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME2)
        product_name1 = product_name1.text
        product_name2 = product_name2.text
        assert product_name1 == product_name2, "Product is'n in basket!" 

    def should_be_basket_total_equal_price_product(self):
        product_price1 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE1)
        product_price2 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE2)
        product_price1 = product_price1.text
        product_price2 = product_price2.text
        assert product_price1 == product_price2, "Basket total dos't equal product price!" 
