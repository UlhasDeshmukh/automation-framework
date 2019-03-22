from pages.mybase_page import MyBasepage

class Loginpage(MyBasepage):

    _username_locator = ('ID', 'login')
    _password_locator = ('ID', 'password')
    _login_button_locator = ('CSS_SELECTOR', 'input.fadeIn.fourth')

    def login(self, username, password):
        self.enter_text(self._username_locator, username)
        self.enter_text(self._password_locator, password)
        self.click(self._login_button_locator)