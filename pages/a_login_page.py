
class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, staff_id, password):
        self.page.locator ("#username").fill(staff_id)
        self.page.locator ("#password").fill(password)
        self.page.locator (".btn-login").click()