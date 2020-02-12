from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, "URL is false" 

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Window for input username is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Window for input password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Window for input email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Window for input password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Window for input password again is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration button is not presented"
