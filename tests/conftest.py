import allure
import pytest
from selene import browser

from pages.events_page import EventsPage
from pages.main_page import MainPage


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://bestdoctor.ru'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()

@pytest.fixture(scope='function', autouse=True)
def open_events_page():
    events_page = EventsPage()
    with allure.step("Открытие страницы Прошедшие вебинары"):
        events_page.open()
    with allure.step("Получить запись"):
        events_page.open_modal_get_record()

    yield events_page


@pytest.fixture(scope='function', autouse=True)
def open_main_page():
    main_page = MainPage()
    with allure.step("Открытие главной страницы"):
        main_page.open()

    yield main_page

