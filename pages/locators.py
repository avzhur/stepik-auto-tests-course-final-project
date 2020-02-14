from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "button[name=login_submit]")
    
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[name=registration_submit]")
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME1 = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME2 = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_PRICE1 = (By.CSS_SELECTOR, "div.product_main p.price_color") 
    PRODUCT_PRICE2 = (By.CSS_SELECTOR, "div.alertinner  p strong")
   
