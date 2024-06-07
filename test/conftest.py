import pytest
from fixture.application import Application
import json
import os.path
from fixture.db import DbFixture


fixture = None
target = None

def load_config(file):
    """
    Вспомогательная функция, которая выполняет загрузку конфигурации
    :param file: файл
    :return: конфгурация
    """
    global target
    if target is None:
        config_file = os.path.abspath(f'../{file}')
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    """
    Функция, которая создаёт фикстуру и выполняет логин
    :param request: специальный параметр
    :return: фикстура (объект класса Application)
    """
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['webadmin']
    web_url = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_url["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    """
    Функция, которая разрушает фикстуру и выполняет логаут
    :param request: специальный параметр
    :return: фикстура (объект класса Application)
    """
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


@pytest.fixture(scope="session")
def db(request):
    """
    Функция, которая создаёт соединение с базой данных приложения, а затем закрывает его
    :param request: специальный параметр
    :return: фикстура (объект класса DbFixture)
    """
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                          password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

