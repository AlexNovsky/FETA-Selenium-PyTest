import pytest


@pytest.mark.home_page
class TestHomePage:
    email = 'pythonminutes@gmail.com'
    password = 'pythonMinutes1'
    def test_home_page_is_opened(self, app):
        page = app.home_page
        page.open_home_page()
        assert page.get_title() == 'Disney.com | The official home for all things Disney'

    def test_home_page_elements(self, app):
        page = app.home_page
        assert page.main_page_check_elements() == True

    def test_banner_is_displayed(self, app):
        page = app.home_page
        assert page.is_banner_displayed() == True

    def test_banner_is_closed(self, app):
        page = app.home_page
        page.close_banner()
        assert page.is_banner_closed()

    def test_signin_is_loaded(self, app):
        page = app.signin_page
        assert page.is_sign_in_loaded() == True
        app.base_page.click(page.sign_in_button)

    def test_signin_frame_visible(self, app):
        page = app.signin_page
        assert page.is_sign_in_frame_displayed() == True

    def test_enter_email_frame_elements(self, app):
        page = app.signin_page
        assert page.enter_email_check_elements() == True

    def test_enter_email(self, app):
        page = app.signin_page
        page.enter_email(self.email)

    def test_password_textbox_loaded(self, app):
        page = app.signin_page
        assert page.is_sign_in_pwd_form_loaded() == True

    def test_enter_password(self, app):
        page = app.signin_page
        page.enter_password(self.password)

    def test_is_user_signed_in(self, app):
        page = app.signin_page
        assert page.is_signed_in() == True

    def test_user_signed_out(self, app):
        page = app.signin_page
        page.sign_out()
        assert page.is_signed_out() == True