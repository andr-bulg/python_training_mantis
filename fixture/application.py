"""
Создаём класс Application, который будет представлять собой фикстуру,
и содержать все необходимые вспомогательные методы.
"""

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper

class Application:

    def __init__(self, browser, config):
        """
        Инициализация фикстуры
        """
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser {}".format(browser))

        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.config = config
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.base_url = config['web']['baseUrl']

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        """
        Разрушение фикстуры
        """
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

