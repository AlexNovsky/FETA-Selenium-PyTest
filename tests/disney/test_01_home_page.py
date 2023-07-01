import pytest
from time import sleep

@pytest.mark.home_page
class TestHomePage:
    def test_home_page_is_opened(self, app):
        page = app.home_page
        page.open_home_page()
        assert page.get_title() == 'Disney.com | The official home for all things Disney'

    def test_home_page_elements(self, app):
        page = app.home_page
        assert all([page.is_displayed(element) for element in page.home_happy_elements])

    def test_banner_is_displayed(self, app):
        page = app.home_page
        assert page.is_banner_displayed() == True

    def test_banner_is_closed(self, app):
        page = app.home_page
        page.close_banner()
        assert page.is_banner_closed()
