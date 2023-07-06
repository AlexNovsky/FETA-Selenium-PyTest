from selenium.webdriver.common.by import By
from resources.common.base_page import BasePage


class SignInPage(BasePage):
    log_in_iframe = (By.CSS_SELECTOR, 'iframe[id="oneid-iframe"]')
    sign_in_button = (By.XPATH, '//a[@class="login-link"]')
    disney_account_img = (By.XPATH, '//*[@id="logo"]')
    enter_email_sign = (By.XPATH, '//*[@id="Title"]')
    enter_email_textbox = (By.XPATH, '//*[@aria-label="Email Address"]')
    submit_email_btn = (By.XPATH, '//button[@data-testid="BtnSubmit"]')
    enter_pwd_sign = (By.XPATH, '//*[@id="Title"]')
    login_email_value = (By.XPATH, '//*[@id="InputLoginValue"]')
    enter_pwd_textbox = (By.XPATH, '//*[@id="InputPassword"]')
    forgot_pwd_btn = (By.XPATH, '//*[@id="HelpSigningIn"]')
    submit_pwd_btn = (By.XPATH, '//button[@data-testid="BtnSubmit"]')
    invalid_email = (By.XPATH, '//*[@id="InputIdentityFlowValue-error"]')
    invalid_pwd = (By.XPATH, '//*[@id="LoginError"]')
    logged_in = (By.XPATH, '//*[@id="goc-user"]//*[@class="goc-login"]//a')
    my_account_btn = (By.XPATH, '//*[@id="goc-user"]//a[@class="login-dropdown-title-link"]')
    account_settings_btn = '//a[@class="login-dropdown-link dropdown_link"]'
    sign_out_btn = (By.XPATH, '//*[@id="goc-user"]//a[@class="login-dropdown-link"]//u')
    signin_happy_elements = [disney_account_img, enter_email_sign]

    def is_sign_in_loaded(self) -> bool:
        """
        Check if sign-in menu is loaded
        :return:        True if frame is displayed
                        False if frame is hidden ot not exist
        """
        if self.is_clickable(self.sign_in_button):
            return True
        else:
            return False

    def enter_email_check_elements(self) -> bool:
        """
        Check that sign-in menu contains "Happy elements"
        :return:        True if frame is displayed
                        False if frame is hidden ot not exist
        """
        self.switch_to_frame(self.log_in_iframe)
        if all([self.is_displayed(element) for element in self.signin_happy_elements]):
            return True
        else:
            return False

    def is_sign_in_frame_displayed(self) -> bool:
        """
        Check if Sign-In frame is shown (popped up) or not with required elements
        :return:        True if frame is displayed and elements are visible
                        False if frame not displayed or required elements not visible
        """
        if bool(self.is_displayed(self.log_in_iframe)):
            return True
        else:
            return False

    def enter_email(self, email):
        """
        Enter the e-mail from variable. Before sending keys, clear the textbox
        :return:        None
        """
        self.click(self.enter_email_textbox)
        self.clear(self.enter_email_textbox)
        self.fill(self.enter_email_textbox, email)
        self.click(self.submit_email_btn)

    def is_sign_in_pwd_form_loaded(self) -> bool:
        """
        Check if enter password frame is shown (popped up) or not with required elements
        :return:        True if frame is displayed and elements are visible
                        False if frame not displayed or required elements not visible
        """
        if bool(self.is_displayed(self.enter_pwd_sign)):
            return True
        else:
            return False

    def enter_password(self, password):
        """
        Enter password from variable. Before sending keys, clear the textbox
        :return:        None
        """
        self.click(self.enter_pwd_textbox)
        self.clear(self.enter_pwd_textbox)
        self.fill(self.enter_pwd_textbox, password)
        self.click(self.submit_pwd_btn)
        self.driver.switch_to.default_content()

    def is_signed_in(self) -> bool:
        """
        Check if user signed in successfully  or not with required elements
        :return:        True if user logged in
                        False if user not logged in
        """
        if bool(self.is_displayed(self.my_account_btn)):
            return True
        else:
            return False

    def sign_out(self) -> None:
        """
        Signing out user
        :return:        None
        """
        self.click(self.my_account_btn)
        if bool(self.is_clickable(self.sign_out_btn)):
            self.click(self.sign_out_btn)

    def is_signed_out(self) -> bool:
        """
        Check if user signed in successfully  or not with required elements
        :return:        True if user logged out
                        False if user still logged in
        """
        if bool(self.is_clickable(self.sign_in_button)):
            signin_button_text = self.get_element_text(self.logged_in)
            if not signin_button_text == 'SIGN IN':
                return False
            else:
                return True
