"""
Создаём класс-помощник ProjectHelper по работе с проектами
"""

from selenium.webdriver.support.ui import Select
import string
import random

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project_obj):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.data_form_completion(project_obj)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def data_form_completion(self, project_obj):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project_obj.project_name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project_obj.status)
        n = self.get_status(project_obj.status)
        wd.find_element_by_xpath("//option[@value='{}']".format(n)).click()
        wd.find_element_by_name("view_state").click()
        n = self.get_view_status(project_obj.view_status)
        wd.find_element_by_xpath("//tr[5]/td[2]/select/option[{}]".format(n)).click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project_obj.description)

    @staticmethod
    def random_name(maxlen):
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for i in range(maxlen)])

    @staticmethod
    def get_view_status(view_status):
        return 1 if view_status == "public" else 2

    @staticmethod
    def get_status(status):
        n = 10
        if status == "release":
            n = 30
        elif status == "stable":
            n = 50
        elif status == "obsolete":
            n = 70
        return n
