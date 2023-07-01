from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base class for every page object of the web application under test
    Includes all basic page methods, applicable to every page, like (is_displayed,
    click, enter_text, get_title, and many more)
    """

    def __init__(self, driver) -> None:
        """Initialize self
        """
        self.driver = driver

    def click(self, locator: WebElement or str or tuple) -> None:
        """Click action on provided element

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def is_displayed(self, locator: WebElement or str or tuple) -> bool:
        """Check if an element with the provided locator is displayed or not

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                True if the element is displayed/visible
                                False if the element is hidden or does not exist
        """
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return bool(element.is_displayed())
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False

    def is_not_displayed(self, locator: WebElement or str or tuple) -> bool:
        """Check if an element with the provided locator is not displayed

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                True if the element is not displayed/visible
                                False if the element is displayed/visible
        """
        try:
            return bool(WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator)))
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False

    def open_url(self, url: str) -> None:
        """Open the provided url in a web browser

        :param url:             String, to be typed into the text field
        :return:                None
        """
        self.driver.get(url)

    def scroll_to(self, locator: WebElement or str or tuple) -> None:
        """Scroll to the provided element. From the nature of this command
            bottom of the element will be at the bottom of the visible part
            of the web page.

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        ActionChains(self.driver).scroll_to_element(locator).perform()

    def hover_to(self, locator: WebElement or str or tuple) -> None:
        """Hover over an element with the provided locator

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        ActionChains(self.driver).move_to_element(locator).perform()

    def select_item_from_dropdown(self, dd_locator: WebElement or str or tuple, item_text: str):
        """Select a drop-down item with the provided text from a drop-down menu with the provided locator

        :param dd_locator:      One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :param item_text:       String, representing the text contained in a drop-down item in a drop-down menu
                                with the provided dd_locator
        :return:                None
        """
        Select(dd_locator).select_by_visible_text(item_text)

    def is_clickable(self, locator: WebElement or str or tuple) -> bool:
        """Check if an element with the provided locator is clickable or not

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                True if the element is displayed
                                False if the element is hidden or does not exist
        """
        try:
            element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
            return bool(element.is_clickable())
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False

    def get_title(self):
        """Return the page title of the currently active browser tab

        :return:                String, representing the page title of the currently active browser tab
        """
        return self.driver.title

    def fill(self, locator: WebElement or str or tuple, text: str) -> None:
        """Typing provided text in the provided text field as login forms etc.

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :param text:            String with the text, which will be sent to the provided text field
        :return:                none
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(locator)
        element.send_keys(text)

    def clear(self, locator: WebElement or str or tuple) -> None:
        """Clear a text field with the provided locator

        :param locator:         One of: - WebElement object
                                        - String Key to find a locator xpath string within page class's attributes
                                        - 2-item tuple containing: (locator strategy, locator identifying string)
        :return:                None
        """
        element = self.driver.find_element(locator).clear()
        element.send_keys(Keys.COMMAND + "a")
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(Keys.BACKSPACE)
