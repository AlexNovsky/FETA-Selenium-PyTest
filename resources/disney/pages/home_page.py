from selenium.webdriver.common.by import By
from resources.common.base_page import BasePage


class HomePage(BasePage):
    home_page_url = "https://www.disney.com/"
    sign_in_button = (By.XPATH, '//a[@class="login-link"]')
    home_page_img = (By.XPATH, '//*[@class="disney-img"]')
    home_page_menu = (By.XPATH, '//*[@id="goc-desktop-global"]')
    banner_iframe = (By.CSS_SELECTOR, 'iframe[aria-label="Advertisement"]')
    banner_close_button = (By.XPATH, '//*[@id="overlay"]//*[@class="sprite close"]')

    home_happy_elements = [home_page_img, home_page_menu]

    def open_home_page(self) -> None:
        """
        Open the provided URL and returning webpage title

        :return:                None
        """
        self.open_url(self.home_page_url)

    def is_banner_displayed(self) -> bool:
        """
        Check if advertisement banner is shown (popped up) or not
        :return:        True if banner is displayed
                        False if banner not displayed
        """
        if self.is_displayed(self.banner_iframe):
            return True
        else:
            return False

    def close_banner(self):
        banner = self.driver.find_element(*self.banner_iframe)
        self.driver.switch_to.frame(banner)
        self.click(self.banner_close_button)
        self.driver.switch_to.default_content()

    def is_banner_closed(self) -> bool:
        """
        Closes advertisement banner on the home page
        :return:        True if banner is closed and  focus return to default content (the web page itself)
                        False if banner still on the screen
        """
        if self.is_not_displayed(self.banner_iframe):
            return True
        else:
            return False
